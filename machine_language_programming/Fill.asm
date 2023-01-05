// Program: Fill.asm
//
// Runs an infinite loop that listens to keyboard input.
// When key pressed, screen is blackened; 
// when no key pressed, screen is cleared.
// Screen remains black or clear as long as the corresponding condition is true.
//
// Usage: press & release any key, observe the response of screen.
//
// Pseudocode:
//   SCREEN_SIZE = 8192 
//   prev_fill = 0
//   fill = 0
//   LOOP:
//     prev_fill = fill
//     if *KBD == 0:
//       fill = 0
//     else:
//       fill = -1
//
//     if fill != prev_fill:
//       for i = 0; i < SCREEN_SIZE; ++i:
//         *(SCREEN + i) = fill
//
//     goto LOOP

// SCREEN_SIZE = 8192
@8192  // 256 x 512 screen, encoded 8192 16-bit values
D=A
@SCREEN_SIZE
M=D
    
// prev_fill = 0
@prev_fill
D=0
M=D

// fill = 0
@fill
D=0
M=D

(MAIN)
  // prev_fill = fill  
  @fill
  D=M
  @prev_fill
  M=D

  // if *KBD == 0:
  //   fill = 0
  // else:
  //   fill = -1
  @KBD
  D=M
  @SET_FILL_TO_CLEAR
  D;JEQ
  @SET_FILL_TO_BLACKEN
  0;JMP
  (SET_FILL_TO_CLEAR)
    @fill
    M=0
    @FILL_SCREEN
    0;JMP
  (SET_FILL_TO_BLACKEN)
    @fill
    M=-1
    @FILL_SCREEN
    0;JMP

  (FILL_SCREEN)
    // if fill != prev_fill:
    @fill
    D=M
    @prev_fill
    D=D-M
    @MAIN
    D;JEQ

    // for i = 0; i < SCREEN_SIZE; ++i:
    //   *(SCREEN + i) = fill
    @i
    M=0
    @SCREEN
    D=A
    @fill_address
    M=D
    (FILL_SCREEN_LOOP)
      // exit if reached the end of the screen
      @SCREEN_SIZE
      D=M
      @i
      D=D-M
      @MAIN
      D;JEQ

      // fill appropriate row of the screen
      @fill
      D=M
      @fill_address
      A=M
      M=D

      // increment fill_address
      @fill_address
      M=M+1

      // increment i
      @i
      M=M+1

      // continue to next iteration
      @FILL_SCREEN_LOOP
      0;JMP

