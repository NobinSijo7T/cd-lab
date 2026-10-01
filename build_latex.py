import os
import subprocess

tex_content = []

# Document preamble - Plain, simple, Times New Roman, no theme
tex_content.append(r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{mathptmx}         % Times New Roman font throughout
\usepackage[top=0.75in, bottom=0.75in, left=1in, right=1in]{geometry}
\usepackage{listings}
\usepackage{needspace}
\usepackage{hyperref}

% Clean black hyperlinks
\hypersetup{
    colorlinks=true,
    linkcolor=black,
    urlcolor=black,
    citecolor=black
}

% Simple plain page style (no headers, page number at bottom center)
\pagestyle{plain}

% Simple listings setup (Times New Roman, no boxes, no line numbers)
\lstset{
    basicstyle=\fontfamily{ptm}\selectfont\normalsize,
    breaklines=true,
    breakatwhitespace=false,
    numbers=none,
    frame=none,
    showstringspaces=false,
    keepspaces=true,
    columns=fullflexible,
    tabsize=4,
    lineskip=-0.8pt
}

\begin{document}
''')

def read_file(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()

# Definition of all 16 experiments
experiments = [
    {
        "num": 1,
        "name": "Design and Implement a Lexical Analyzer using C Language",
        "programs": [
            ("C Program (lexical_analyzer.c)", "01_Lexical_Analyzer_in_C/lexical_analyzer.c")
        ],
        "io": """Enter the input string:
int a = 10 + b;

int : Keyword
a : Identifier
= : Operator
10 : Constant
+ : Operator
b : Identifier
; : Delimiter"""
    },
    {
        "num": 2,
        "name": "Implement a Lexical Analyzer using LEX Tool",
        "programs": [
            ("LEX Specification (lex.l)", "02_Lexical_Analyzer_using_Lex/lex.l")
        ],
        "io": """enter ip: int a float b
keyword identifier keyword identifier"""
    },
    {
        "num": 3,
        "name": "Display Number of Lines, Words, Spaces, and Characters using LEX",
        "programs": [
            ("LEX Specification (lines.l)", "03_Count_Lines_Words_Characters/lines.l")
        ],
        "io": """Enter the input:
Hello world
This is compiler design lab

The number of lines=2
The number of spaces=5
The number of words=7
The number of characters are=40"""
    },
    {
        "num": 4,
        "name": "Convert Substring 'abc' to 'ABC' using LEX",
        "programs": [
            ("LEX Specification (sub.l)", "04_Replace_Substring_abc_to_ABC/sub.l")
        ],
        "io": """Input: welcome to abc lab
Output: welcome to ABC lab"""
    },
    {
        "num": 5,
        "name": "Count Vowels and Consonants using LEX",
        "programs": [
            ("LEX Specification (vowels.l)", "05_Count_Vowels_and_Consonants/vowels.l")
        ],
        "io": """Enter string: Engineering
Vowels: 5
Consonants: 6"""
    },
    {
        "num": 6,
        "name": "Valid Arithmetic Expression using YACC",
        "programs": [
            ("Lexer Specification (prg6.l)", "06_Valid_Arithmetic_Expression_YACC/prg6.l"),
            ("YACC Parser Specification (prg6.y)", "06_Valid_Arithmetic_Expression_YACC/prg6.y")
        ],
        "io": """Enter an arithmetic expression: (5+3)*2-4/2

Result=14

Entered Arithmetic expression is valid""",
        "clearpage_output": True
    },
    {
        "num": 7,
        "name": "Valid Identifier using YACC",
        "programs": [
            ("Lexer Specification (prg5.l)", "07_Valid_Identifier_YACC/prg5.l"),
            ("YACC Parser Specification (prg5.y)", "07_Valid_Identifier_YACC/prg5.y")
        ],
        "io": """enter identifier: abc
Valid Identifier."""
    },
    {
        "num": 8,
        "name": "Calculator using LEX and YACC",
        "programs": [
            ("Lexer Specification (calculator.l)", "08_Calculator_using_Lex_and_YACC/calculator.l"),
            ("YACC Parser Specification (calculator.y)", "08_Calculator_using_Lex_and_YACC/calculator.y")
        ],
        "io": """Enter Any Arithmetic Expression which can have operations Addition, Subtraction, Multiplication, Division, Modulus and Round brackets:
15+4*3-(10/2)

Result=22

Entered arithmetic expression is Valid"""
    },
    {
        "num": 9,
        "name": "Epsilon Closure of States in NFA",
        "programs": [
            ("Source Code (epsilon.c)", "09_Epsilon_Closure/epsilon.c")
        ],
        "io": """Enter the no of states: 3
Enter the states: 0 1 2

Epsilon closure of 0 = {0, 1, 2}

Epsilon closure of 1 = {1, 2}

Epsilon closure of 2 = {2}"""
    },
    {
        "num": 10,
        "name": "Conversion of NFA to DFA",
        "programs": [
            ("Source Code (dfa.c)", "10_NFA_to_DFA/dfa.c")
        ],
        "io": """Enter No of alphabets and alphabets:
2
a
b
Enter the number of states:
3
Enter the start state:
1
Enter the number of final states:
1
Enter the final states:
3
Enter no of transition:
4
NOTE:- [Transition is in the form-> qno alphabet qno]
NOTE:- [States number must be greater than zero]

Enter transition:
1 a 1
1 a 2
1 b 1
2 b 3

Equivalent DFA.....
Transitions of DFA
{q1,}   a   {q1,q2,}
{q1,}   b   {q1,}
{q1,q2,}   a   {q1,q2,}
{q1,q2,}   b   {q1,q3,}
{q1,q3,}   a   {q1,q2,}
{q1,q3,}   b   {q1,}

States of DFA:
{q1,}   {q1,q2,}   {q1,q3,}

Alphabets:
a   b

Start State:
q1

Final states:
{q1,q3,}""",
        "clearpage_output": True
    },
    {
        "num": 11,
        "name": "Minimization of DFA",
        "programs": [
            ("Source Code (minimisation.c)", "11_DFA_Minimization/minimisation.c")
        ],
        "io": """Enter the number of states: 5
Enter number of symbols: 2
Enter the transition (-1 for no transition):
Transition from state 0 on symbol 0: 1
Transition from state 0 on symbol 1: 2
Transition from state 1 on symbol 0: 1
Transition from state 1 on symbol 1: 3
Transition from state 2 on symbol 0: 1
Transition from state 2 on symbol 1: 2
Transition from state 3 on symbol 0: 1
Transition from state 3 on symbol 1: 4
Transition from state 4 on symbol 0: 1
Transition from state 4 on symbol 1: 2
Enter the no. of final states: 1
Enter the final states:
4

Minimized DFA:
Total minimized states: 4

State 0:
  On symbol 0 -> State 1
  On symbol 1 -> State 0

State 1:
  On symbol 0 -> State 1
  On symbol 1 -> State 2

State 2:
  On symbol 0 -> State 1
  On symbol 1 -> State 3

State 3 (Final):
  On symbol 0 -> State 1
  On symbol 1 -> State 0""",
        "clearpage_output": True
    },
    {
        "num": 12,
        "name": "Computation of FIRST and FOLLOW Sets",
        "programs": [
            ("Source Code (FF.c)", "12_First_and_Follow/FF.c")
        ],
        "io": """Enter the no of productions:
3
Enter the  productions:
S=Ab
A=a
A=#
Enter the elements whose first and follow is to be found: S
First(S)={a#}
Follow(S)={$}
Continue(0/1)? 1
Enter the elements whose first and follow is to be found: A
First(A)={a#}
Follow(A)={b}
Continue(0/1)? 0"""
    },
    {
        "num": 13,
        "name": "Recursive Descent Parser",
        "programs": [
            ("Source Code (recursive.c)", "13_Recursive_Descent_Parser/recursive.c")
        ],
        "io": """Enter an arithmetic expression: a+b
Accepted""",
        "clearpage_output": True
    },
    {
        "num": 14,
        "name": "Shift Reduce Parser",
        "programs": [
            ("Source Code (shift.c)", "14_Shift_Reduce_Parser/shift.c")
        ],
        "io": """Enter the number of production rules: 3
Enter the number of production rules(in the form of left->right):
E->E+E
E->E*E
E->a

Enter the input string: a+a*a
a       +a*a    Shift a
E       +a*a    Reduce E-> a
E+      a*a     Shift +
E+a     *a      Shift a
E+E     *a      Reduce E-> a
E       *a      Reduce E-> E+E
E*      a       Shift *
E*a             Shift a
E*E             Reduce E-> a
E               Reduce E-> E*E

Accepted""",
        "io_latex": r"""\begin{lstlisting}
Enter the number of production rules: 3
Enter the number of production rules(in the form of left->right):
E->E+E
E->E*E
E->a

Enter the input string: a+a*a
\end{lstlisting}
\vspace{0.2em}
{\setlength{\tabcolsep}{16pt}
\noindent\begin{tabular}{@{}lll@{}}
a & +a*a & Shift a \\
E & +a*a & Reduce E-> a \\
E+ & a*a & Shift + \\
E+a & *a & Shift a \\
E+E & *a & Reduce E-> a \\
E & *a & Reduce E-> E+E \\
E* & a & Shift * \\
E*a & & Shift a \\
E*E & & Reduce E-> a \\
E & & Reduce E-> E*E \\
\end{tabular}}
\vspace{0.4em}
\begin{lstlisting}
Accepted
\end{lstlisting}"""
    },
    {
        "num": 15,
        "name": "Constant Propagation (Code Optimization)",
        "programs": [
            ("Source Code (constant_propagation.c)", "15_Constant_Propagation/constant_propagation.c")
        ],
        "io": """Enter the number of expressions: 3

Enter the input:

= 3 - a

+ a t1 t2

* t2 a t3

The optimized code is:

+ 3 t1 t2

* t2 3 t3""",
        "clearpage_output": True
    },
    {
        "num": 16,
        "name": "Intermediate Code Generation (Three-Address Code)",
        "programs": [
            ("Source Code (icg.c)", "16_Intermediate_Code_Generation/icg.c")
        ],
        "io": """Enter the infix expression: a+(b*c)-d
Postfix expression: abc*d-+

Operator    op1    op2    result
---------------------------------
*           b      c      t1

-           t1     d      t2

+           a      t2     t3""",
        "io_latex": r"""\begin{lstlisting}
Enter the infix expression: a+(b*c)-d
Postfix expression: abc*d-+
\end{lstlisting}
\vspace{0.3em}
{\setlength{\tabcolsep}{22pt}
\noindent\begin{tabular}{@{}llll@{}}
Operator & op1 & op2 & result \\[0.1em]
\multicolumn{4}{@{}l@{}}{------------------------------------------------------------} \\
{}* & b & c & t1 \\[0.8em]
-- & t1 & d & t2 \\[0.8em]
+ & a & t2 & t3 \\
\end{tabular}}"""
    }
]

for exp in experiments:
    num = exp["num"]
    name = exp["name"]
    if num > 1:
        tex_content.append("\\clearpage\n")
    tex_content.append(f"\\noindent\\textbf{{\\large Program Name:}} {name}\\par\\vspace{{0.6em}}\n")
    tex_content.append(f"\\noindent\\textbf{{\\large Program:}}\\par\\vspace{{0.3em}}\n")
    
    if len(exp["programs"]) == 1:
        title, filepath = exp["programs"][0]
        code = read_file(filepath)
        tex_content.append("\\begin{lstlisting}\n")
        tex_content.append(code.rstrip())
        tex_content.append("\n\\end{lstlisting}\n\n")
    else:
        for title, filepath in exp["programs"]:
            code = read_file(filepath)
            tex_content.append(f"\\noindent\\textbf{{{title}:}}\\par\\vspace{{0.2em}}\n")
            tex_content.append("\\begin{lstlisting}\n")
            tex_content.append(code.rstrip())
            tex_content.append("\n\\end{lstlisting}\n\n")
    
    if exp.get("clearpage_output"):
        tex_content.append("\\clearpage\n")
    else:
        io_lines = exp["io"].strip().count('\n') + 1
        needlines = min(8, max(4, io_lines + 2))
        tex_content.append(f"\\needspace{{{needlines}\\baselineskip}}\n")
        tex_content.append("\\vspace{0.6em}\n")
    tex_content.append("\\noindent\\textbf{\\underline{Output:}}\\par\\vspace{0.4em}\n")
    if "io_latex" in exp:
        tex_content.append(exp["io_latex"].strip() + "\n\n")
    else:
        tex_content.append("\\begin{lstlisting}\n")
        tex_content.append(exp["io"].strip())
        tex_content.append("\n\\end{lstlisting}\n\n")

tex_content.append(r"\end{document}" + "\n")

full_tex = "".join(tex_content)
with open("Compiler_Design_Lab_Record.tex", "w", encoding="utf-8") as f:
    f.write(full_tex)

print("Generated Compiler_Design_Lab_Record.tex successfully!")

print("Compiling LaTeX to PDF...")
subprocess.run(["pdflatex", "-interaction=nonstopmode", "Compiler_Design_Lab_Record.tex"], check=True)
print("Compiler_Design_Lab_Record.pdf generated successfully!")
