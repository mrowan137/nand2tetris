"""
Module for translating C-command fields (which are of the form `dest=comp;jump`)
to corresponding HACK machine code. The module contains a class `Code` with the
following methods:
* `__init__(self)`: initialize mappings from destination, comparison, and jump
  fields to HACK machine code.
* `Dest(self, dest)`: return the HACK machine code corresponding to `dest`,
  where `dest` is a valid destination symbol.
* `Comp(self, comp)`: return the HACK machine code corresponding to `comp`,
  where `comp` is a valid comparison symbol.
* `Jump(self, jump)`: return the HACK machine code corresponding to `jump`,
  where `jump` is a valid jump symbol.

Example usage:

```python
>>> machine_code = "111"
>>> code = Code()
>>> comp = code.Comp("D")
>>> dest = code.Dest("null")
>>> jump = code.Jump("JGT")
>>> machine_code += (comp + dest + jump)
>>> print(machine_code)
1110001100000001
```

This example converts the HACK assembly C-command `D;JGT` to HACK machine code.
By piecing together translations for the `comp`, `dest` (`null`, in this case),
and `jump` fields (0001100, 000, and  001, respectively), the `Code` class
generates corresponding HACK machine code.
"""


class Code:
  """
  `Code` class is a tool for converting HACK C-commands (`dest=comp;jump`) to
  HACK machine code. The class contains mappings from valid selections for the
  comparison, destination, and jump fields of a HACK assembly C-command, to
  corresponding HACK machine code. The individual mappings can be used to
  produce the full translation of a given HACK assembly C-command to its
  counterpart HACK machine code.
  """
  def __init__(self):
    """
    Initialize mappings from HACK assembly C-command fields destination,
    comparison, and jump (`dest=comp;jump`) to corresponding HACK machine code.
    """
    self.dest_to_bits_ = {
      "null" : "000",
      "M"    : "001",
      "D"    : "010",
      "MD"   : "011",
      "A"    : "100",
      "AM"   : "101",
      "AD"   : "110",
      "AMD"  : "111"
    }

    self.comp_to_bits_ = {
        "0"   : "0101010",
        "1"   : "0111111",
        "-1"  : "0111010",
        "D"   : "0001100",
        "A"   : "0110000",
        "M"   : "1110000",
        "!D"  : "0001101",
        "!A"  : "0110001",
        "!M"  : "1110001",
        "-D"  : "0001111",
        "-A"  : "0110011",
        "-M"  : "1110011",
        "D+1" : "0011111",
        "A+1" : "0110111",
        "M+1" : "1110111",
        "D-1" : "0001110",
        "A-1" : "0110010",
        "M-1" : "1110010",
        "D+A" : "0000010",
        "D+M" : "1000010",
        "D-A" : "0010011",
        "D-M" : "1010011",
        "A-D" : "0000111",
        "M-D" : "1000111",
        "D&A" : "0000000",
        "D&M" : "1000000",
        "D|A" : "0010101",
        "D|M" : "1010101"
    }

    self.jump_to_bits_ = {
      "null" : "000",
      "JGT"  : "001",
      "JEQ"  : "010",
      "JGE"  : "011",
      "JLT"  : "100",
      "JNE"  : "101",
      "JLE"  : "110",
      "JMP"  : "111"
    }

  def Dest(self, dest):
    """
    Converts HACK assembly C-command `dest` field to its corresponding HACK
    machine code.
    """
    return self.dest_to_bits_[dest] if dest in self.dest_to_bits_ else None

  def Comp(self, comp):
    """
    Converts HACK assembly C-command `comp` field to its corresponding HACK
    machine code.
    """
    return self.comp_to_bits_[comp] if comp in self.comp_to_bits_ else None

  def Jump(self, jump):
    """
    Converts HACK assembly C-command `jump` field to its corresponding HACK
    machine code.
    """
    return self.jump_to_bits_[jump] if jump in self.jump_to_bits_ else None
