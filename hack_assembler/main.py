"""
Driver code for HACK assembler.
Takes input HACK assembly file and converts to HACK machine code.
The input program is assumed to be error-free HACK assembly language.
Example usage:

```python
>>> python main.py my_program.asm > my_program.hack
```

"""

import sys

from hack_assembler.hack_assembler import HackAssembler


try:
  hack_asm_file = sys.argv[1]
except IndexError:
  print("Error: no file name provided; usage:\n"
        "python main.py my_hack_program.asm\n")

hack_assembler = HackAssembler(hack_asm_file)

if __name__ == "__main__":
  hack_assembler.Run()
