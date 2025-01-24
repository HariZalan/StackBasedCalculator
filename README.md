# StackBasedCalculator
It is a calculator using Reverse Polish Notation written in Python, with loops and conditionals. The commands are:
| Command | Function |
| ------------- | -------------
| + | Pops two values off the stack, adds them, then pushes the result back.
| - | Pops two values off the stack, substracts the first from the second, then pushes the result back.
| * | Pops two values off the stack, multiplies them, then pushes the result back.
| / | Pops two values off the stack, divides the second by the first, then pushes the result back.
| d | Duplicates the top value.
| e | „Executes” the top value (i. e. interprets it as a series of commands)
| ri | Moves the top value to register i.
| Ri | Vice versa.
| p | Prints the top value.
| =i | Pops off two values, and if they are equal, moves a third one to register i.
| <i | Pops off two values, and if the first is greater than the second, moves a third one to register i.
## Syntax

Commands must be separated with spaces. In order to prevent them from being immediately executed, and put them on the stack (where you can use "e"), substitute spaces with underscores. 

## Examples
3 + 4:
`3 4 + p`

Print even numbers with an infinite loop:

`0 p ri_2_+_p_Ri_d_e d e`

Print Fibonacci numbers indefinitely:

`0 1 ri_rj_rk_Rj_d_Rk_+_p_Ri_d_e d e`

Pointless loop slowly taking memory up:
`d_e d e`

## Usage

You can use the calculator with

`python3 ./calc "the code to execute"`
