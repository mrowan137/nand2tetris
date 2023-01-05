"""
Module to store symbol-to-address (ROM or RAM) mappings.
The module contains a class `SymbolTable` which initializes predefined HACK
symbol-to-address mappings, and can be updated with label or variable addresses
as needed. `SymbolTable` has the following methods:
* `__init__(self)`: initialize symbol table with all pre-defined HACK symbols,
  and index to first available RAM address.
* `__call__(self, symbol)`: returns the address corresponding to `symbol`, if
  present in the symbol table.
* `AddRAMEntry(self, symbol)`: add symbol table entry for new variable at next
  available RAM address.
* `Contains(self, symbol)`: returns `true` if `symbol` is a present in the
  symbol table, otherwise `false`.

Example usage:

```python
>>> symbol_table = SymbolTable()
>>> print(symbol_table("SCREEN"))
16384
>>> symbol_table.AddRAMEntry("x")
>>> print(symbol_table("x"))
16
```

The example shows e.g. that the screen "SCREEN" RAM address is initialized to
begin at 16384 (as per HACK specification), and a variable `x` has the address
16 in RAM, as it is added to the first available RAM address.
"""


class SymbolTable:
  """
  `SymbolTable` contains a mapping from HACK assembly labels or variables to
  the corresponding ROM or RAM address. The mapping comes pre-populated with
  HACK symbols according to HACK specification, and can be updated as labels
  or variables are encountered in a HACK assembly code.
  """
  def __init__(self):
    """
    Initialize symbol table with all pre-defined HACK symbols, and index to
    first available RAM address.
    """
    self.symbol_to_address_ = {
      "SP"     : 0,
      "LCL"    : 1,
      "ARG"    : 2,
      "THIS"   : 3,
      "THAT"   : 4,
      "R0"     : 0,
      "R1"     : 1,
      "R2"     : 2,
      "R3"     : 3,
      "R4"     : 4,
      "R5"     : 5,
      "R6"     : 6,
      "R7"     : 7,
      "R8"     : 8,
      "R9"     : 9,
      "R10"    : 10,
      "R11"    : 11,
      "R12"    : 12,
      "R13"    : 13,
      "R14"    : 14,
      "R15"    : 15,
      "SCREEN" : 16384,
      "KBD"    : 24576
    }

    # track next valid address where variable could be stored
    self.next_available_ram_address_ = 16

  def __call__(self, symbol):
    """
    Returns the address corresponding to `symbol`, if it's present in the
    symbol table; allows for convenient usage `x_addr = symbol_table("x")` where
    `symbol_table` is a `SymbolTable` object.
    """
    return (self.symbol_to_address_[symbol]
      if symbol in self.symbol_to_address_ else None)

  def AddEntry(self, symbol, address):
    """
    Add symbol and address.
    """
    self.symbol_to_address_[symbol] = address

  def AddRAMEntry(self, symbol):
    """
    Add symbol table entry for new variable at next available RAM address.
    """
    self.symbol_to_address_[symbol] = self.next_available_ram_address_
    self.next_available_ram_address_ += 1

  def Contains(self, symbol):
    """
    Returns `true` if `symbol` is a present in the symbol table, else `false`.
    """
    return symbol in self.symbol_to_address_
