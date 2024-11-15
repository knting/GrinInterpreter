This project implements an interpreter for the Grin programming language, a simple, line-by-line interpreted language designed to perform basic programming operations. 
The Grin language includes functionality for variable manipulation, arithmetic operations, control flow, and subroutines. 
The interpreter is built in Python, using modular design principles and an object-oriented approach, with robust unit testing to ensure correctness.

**Features**
Lexical Analysis: Tokenizes Grin statements into lexemes (e.g., keywords, identifiers, literals).
Parsing: Converts Grin statements into executable operations.
Execution: Interprets and executes Grin programs with support for:
Variable assignments and manipulations (LET, ADD, SUB, MULT, DIV)
Input and output operations (PRINT, INNUM, INSTR)
Control flow (GOTO, IF, GOSUB, RETURN)
Program termination (END, .)
Error Handling: Detects and reports lexical, syntactic, and runtime errors.
Unit Testing: Includes comprehensive unit tests for all components, such as lexing, parsing, and execution.


**Example**
LET A 1
GOSUB 5
PRINT A
END
LET A 3
RETURN
PRINT A
LET A 2
GOSUB -4
PRINT A
RETURN
.

would return:
1
3
3
