# nand2tetris

Personal work and projects for
[nand2tetris course](https://www.coursera.org/learn/build-a-computer), offered
by Hebrew University of Jerusalem through Coursera.


## Description

Contents of the repository are as follows:
* [boolean_logic](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic):
  [HDL (Hardware Description Language)](https://drive.google.com/file/d/1dPj4XNby9iuAs-47U9k3xtYy9hJ-ET0T/view)
  implementations of elementary logic gates:
  * [And.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/And.hdl)
  * [Or.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Or.hdl)
  * [Xor.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Xor.hdl)
  * [Mux.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Mux.hdl)
  * [DMux.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/DMux.hdl)
  * [Not16.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Not16.hdl)
  * [And16.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/And16.hdl)
  * [Or16.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Or16.hdl)
  * [Mux16.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Mux16.hdl)
  * [Or8Way.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Or8Way.hdl)
  * [Mux4Way16.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Mux4Way16.hdl)
  * [Mux8Way16.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/Mux8Way16.hdl)
  * [DMux4Way.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/DMux4Way.hdl)
  * [DMux8Way.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_logic/DMux8Way.hdl)
* [boolean_arithmetic](https://github.com/mrowan137/nand2tetris/blob/main/boolean_arithmetic):
  HDL implementations of set of chips which together lead to HACK ALU:
  * [HalfAdder.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_arithmetic/HalfAdder.hdl)
  * [FullAdder.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_arithmetic/FullAdder.hdl)
  * [Add16.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_arithmetic/Add16.hdl)
  * [Inc16.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_arithmetic/Inc16.hdl)
  * [ALU.hdl](https://github.com/mrowan137/nand2tetris/blob/main/boolean_arithmetic/ALU.hdl)
* [memory](https://github.com/mrowan137/nand2tetris/blob/main/memory):
  HDL implementation of main RAM memory unit of HACK computer:
  * [Bit.hdl](https://github.com/mrowan137/nand2tetris/blob/main/memory/Bit.hdl)
  * [Register.hdl](https://github.com/mrowan137/nand2tetris/blob/main/memory/Register.hdl)
  * [RAM8.hdl](https://github.com/mrowan137/nand2tetris/blob/main/memory/RAM8.hdl)
  * [RAM64.hdl](https://github.com/mrowan137/nand2tetris/blob/main/memory/RAM64.hdl)
  * [RAM512.hdl](https://github.com/mrowan137/nand2tetris/blob/main/memory/RAM512.hdl)
  * [RAM4K.hdl](https://github.com/mrowan137/nand2tetris/blob/main/memory/RAM4K.hdl)
  * [RAM16K.hdl](https://github.com/mrowan137/nand2tetris/blob/main/memory/RAM16K.hdl)
  * [PC.hdl](https://github.com/mrowan137/nand2tetris/blob/main/memory/PC.hdl)  
* [machine_language_programming](https://github.com/mrowan137/nand2tetris/blob/main/machine_language_programming):
  HACK assembly language programs:
  * [Mult.asm](https://github.com/mrowan137/nand2tetris/blob/main/machine_language_programming/Mult.asm)
  * [Fill.asm](https://github.com/mrowan137/nand2tetris/blob/main/machine_language_programming/Fill.asm)
* [computer_architecture](https://github.com/mrowan137/nand2tetris/blob/main/computer_architecture):
  HDL implementation of the HACK computer, composed of ROM & main RAM memory
  unit, and CPU:
  * [Memory.hdl](https://github.com/mrowan137/nand2tetris/blob/main/computer_architecture/Memory.hdl)
  * [CPU.hdl](https://github.com/mrowan137/nand2tetris/blob/main/computer_architecture/CPU.hdl)
* [hack_assembler](https://github.com/mrowan137/nand2tetris/blob/main/hack_assembler):
  HACK assembler that can convert error-free HACK assembly language to
  corresponding HACK machine code.


## Author

Michael E. Rowan — [mrowan137](https://github.com/mrowan137) — [michael@mrowan137.dev](mailto:michael@mrowan137.dev).


## License

[MIT License](https://github.com/mrowan137/connect-k/LICENSE).


## Acknowledgments

* [Build a Modern Computer from First Principles: From Nand to Tetris (Project-Centered Course)](https://www.coursera.org/learn/build-a-computer)
* [nand2tetris](https://www.nand2tetris.org/)
* [HDL (Hardware Description Language) guide](https://drive.google.com/file/d/1dPj4XNby9iuAs-47U9k3xtYy9hJ-ET0T/view)
* [HACK chip set](https://drive.google.com/file/d/1IsDnH0t7q_Im491LQ7_5_ajV0CokRbwR/view)
* Fantastic instructors of the nand2tetris course: [Noam Nisan](https://www.cs.huji.ac.il/~noam/), [Shimon Schocken](https://www.shimonschocken.com/)
