// Program: Mult.asm
//
// Multiply R0 and R1, store result in R2.
// R0, R1, and R2 refer to RAM[0], RAM[1], and RAM[2], respectively.
// This program handles arguments where R0 and R1 are non-negative
// and the result of the multiplication is less than 32768.
//
// Usage: put numbers into R0 and R1.
//
// Pseudocode:
//   i = R1
//   R2 = 0
//
//   LOOP:
//     if i == 0: goto END
//     R2 += R0
//     i -= 1
   
// i = R1
@R1
D=M
@i
M=D

// R2 = 0
@R2
M=0

(LOOP)
  // if i == 0 goto END
  @i
  D=M
  @END
  D;JEQ

  // R2 += R0
  @R2  
  D=M
  @R0
  D=D+M
  @R2
  M=D

  // i -= 1
  @i
  D=M
  D=D-1
  M=D
    
  @LOOP
  0;JMP

(END)
  @END
  0;JMP
