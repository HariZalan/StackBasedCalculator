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

