"""
Module for HACK assembly language to HACK machine code conversion.
The module contains a class `HackAssembler` that can be used to convert
(assumed error-free) HACK assembly code to its corresponding HACK machine code.
`HackAssembler` class has the following methods:
* `__init__(self, hack_asm_file)`: initializes the class with `Parser`, `Code`,
  and `SymbolTable` objects for parsing input HACK assembly file
  (`hack_asm_file`), assembly translation to machine code, and mapping label &
  variables to addresses, respectively.
* `Run(self)`: converts input HACK assembly file `hack_asm_file` to machine
  code, via two passes `FirstPass` and `SecondPass`.
* `FirstPass(self)`: Store into symbol table mappings from label to ROM address.
* `SecondPass(self)`: Store into symbol table mappings from variable to RAM
  address, and computes (line-by-line) translation of the input HACK assembly.

Example usage:

```python
>>> hack_assembler = HackAssembler(hack_asm_file)
>>> hack_assembler.Run()
```

This will print out the resulting HACK machine code, which could be redirected
to an output file.
"""
from hack_assembler.parser import Parser
from hack_assembler.code import Code
from hack_assembler.symbol_table import SymbolTable


class HackAssembler:
  """
  `HackAssembler` class is a tool for translating HACK assembly language into
  HACK machine code. It computes the output machine code via two passes, a first
  to convert labels to ROM address, then a second to convert variables to RAM
  addresses, and complete the translation; label and variable addresses are
  logged in a symbol table.
  """
  def __init__(self, hack_asm_file):
    """
    Initializes `HackAssembler` with `Parser`, `SymbolTable`, and `Code` members
    for parsing input HACK assembly, storing mapping from label & variable to
    addresses, and Hack assembly language translation, respectively.
    """
    self.parser_ = Parser(hack_asm_file)
    self.symbol_table_ = SymbolTable()
    self.code_ = Code()
    self.output_ = ""

  def Run(self):
    """
    Convert the input HACK assembly to HACK machine code.
    """
    self.FirstPass()
    self.SecondPass()

  def FirstPass(self):
    """
    Store label to ROM address into symbol table.
    """
    # track the ROM address a command is eventually loaded to
    rom_address = -1
    while self.parser_.HasMoreCommands():
      self.parser_.Advance()
      if (   self.parser_.CommandType() == "A_COMMAND"
          or self.parser_.CommandType() == "C_COMMAND"):
        rom_address += 1
      else:  # L-command
        self.symbol_table_.AddEntry(self.parser_.Symbol(),
                                    rom_address + 1)

    # leave the parser how we found it
    self.parser_.Reset()

  def SecondPass(self):
    """
    Store variable to RAM address into symbol table.
    """
    while self.parser_.HasMoreCommands():
      machine_code = ""

      self.parser_.Advance()

      if self.parser_.CommandType() == "A_COMMAND":
        machine_code += "0"
        rest = self.parser_.Symbol()
        if not rest.isdigit():
          if not self.symbol_table_.Contains(rest):
            # symbol needs to be added to table if not there
            self.symbol_table_.AddRAMEntry(rest)

          rest = str(self.symbol_table_(rest))

        # finish the translation
        machine_code += str(bin(int(rest)))[2:].zfill(15)

      elif self.parser_.CommandType() == "C_COMMAND":
        machine_code += "111"

        # extract fields from current C-command
        comp = self.parser_.Comp()
        dest = self.parser_.Dest()
        jump = self.parser_.Jump()

        # translate
        comp = self.code_.Comp(comp)
        dest = self.code_.Dest(dest)
        jump = self.code_.Jump(jump)

        machine_code += (comp + dest + jump)

      else:  # L-command
        pass

      if machine_code: self.output_ += (machine_code + "\n")

    # remove the last newline
    print(self.output_[:-1])
