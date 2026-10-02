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

# Formatted overrides for LaTeX PDF output (ensures proper tabbing to identify loops without touching source files)
FORMATTED_CODE_FOR_LATEX = {
    "12_First_and_Follow/FF.c": r"""#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int n, m = 0, p, i = 0, j = 0;
char a[10][10], f[10];
void follow(char c);
void first(char c);

int main()
{
    int i, z;
    char c, ch;
    printf("Enter the no of productions:\n");
    scanf("%d", &n);
    printf("Enter the  productions:\n");
    for (i = 0; i < n; i++)
        scanf("%s%c", a[i], &ch);
    do
    {
        m = 0;
        printf("Enter the elements whose first and follow is to be found:");
        scanf("%c", &c);
        first(c);
        printf("First(%c)={", c);
        for (i = 0; i < m; i++)
            printf("%c", f[i]);
        printf("}\n");
        strcpy(f, " ");
        m = 0;
        follow(c);
        printf("Follow(%c)={", c);
        for (i = 0; i < m; i++)
            printf("%c", f[i]);
        printf("}\n");
        printf("Continue(0/1)?");
        scanf("%d%c", &z, &ch);
    } while (z == 1);
    return (0);
}

void first(char c)
{
    int k;
    if (!isupper(c))
        f[m++] = c;
    for (k = 0; k < n; k++)
    {
        if (a[k][0] == c)
        {
            if (a[k][2] == '#')
                f[m++] = '#';
            else if (islower(a[k][2]))
                f[m++] = a[k][2];
            else
                first(a[k][2]);
        }
    }
}

void follow(char c)
{
    if (a[0][0] == c)
        f[m++] = '$';
    for (i = 0; i < n; i++)
    {
        for (j = 2; j < strlen(a[i]); j++)
        {
            if (a[i][j] == c)
            {
                if (a[i][j + 1] != '\0')
                    first(a[i][j + 1]);
                if (a[i][j + 1] == '\0' && c != a[i][0])
                    follow(a[i][0]);
            }
        }
    }
}""",

    "14_Shift_Reduce_Parser/shift.c": r"""#include <stdio.h>
#include <string.h>

struct ProductionRule
{
    char left[10];
    char right[10];
};

int main()
{
    char input[20], stack[50], temp[50], ch[2], *token1, *token2, *substring;
    int i, j, stack_length, substring_length, stack_top, rule_count = 0;
    struct ProductionRule rules[10];

    stack[0] = '\0';

    printf("\nEnter the number of production rules:");
    scanf("%d", &rule_count);

    printf("\nEnter the number of production rules(in the form of left->right):\n");
    for (i = 0; i < rule_count; i++)
    {
        scanf("%s", temp);
        token1 = strtok(temp, "->");
        token2 = strtok(NULL, "->");
        strcpy(rules[i].left, token1);
        strcpy(rules[i].right, token2);
    }

    printf("\nEnter the input string:");
    scanf("%s", input);

    i = 0;
    while (1)
    {
        if (i < strlen(input))
        {
            ch[0] = input[i];
            ch[1] = '\0';
            i++;
            strcat(stack, ch);
            printf("%s\t", stack);
            for (int k = i; k < strlen(input); k++)
            {
                printf("%c", input[k]);
            }
            printf("\tShift %s\n", ch);
        }

        for (j = 0; j < rule_count; j++)
        {
            substring = strstr(stack, rules[j].right);
            if (substring != NULL)
            {
                stack_length = strlen(stack);
                substring_length = strlen(substring);
                stack_top = stack_length - substring_length;
                stack[stack_top] = '\0';
                strcat(stack, rules[j].left);
                printf("%s\t", stack);
                for (int k = i; k < strlen(input); k++)
                {
                    printf("%c", input[k]);
                }
                printf("\tReduce %s-> %s\n", rules[j].left, rules[j].right);
                j = -1;
            }
        }

        if (strcmp(stack, rules[0].left) == 0 && i == strlen(input))
        {
            printf("\nAccepted\n");
            break;
        }

        if (i == strlen(input))
        {
            printf("\nNot Accepted\n");
            break;
        }
    }

    return 0;
}""",

    "04_Replace_Substring_abc_to_ABC/sub.l": r"""%{
#include <stdio.h>
%}

%%
"abc" {printf("ABC");}
. {putchar(yytext[0]);}
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}""",

    "09_Epsilon_Closure/epsilon.c": r"""#include <stdio.h>
#include <string.h>

char states[20][20];
char result[20][20];
char copy[20];

int is_present(char state[20], int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (strcmp(result[i], state) == 0)
            return 1;
    }
    return 0;
}

void epsilon_closure(char start[20], FILE *INPUT)
{
    char current[20];
    char state1[20], input[20], state2[20];
    int count = 0;
    int i;

    strcpy(copy, start);
    strcpy(result[count++], start);
    i = 0;
    while (i < count)
    {
        strcpy(current, result[i]);
        rewind(INPUT);
        while (fscanf(INPUT, "%s %s %s", state1, input, state2) == 3)
        {
            if (strcmp(current, state1) == 0 && strcmp(input, "e") == 0)
            {
                if (!is_present(state2, count))
                {
                    strcpy(result[count++], state2);
                }
            }
        }
        i++;
    }

    printf("\nEpsilon closure of %s = {", copy);
    for (i = 0; i < count; i++)
    {
        printf("%s", result[i]);
        if (i < count - 1)
            printf(", ");
    }
    printf("}\n");
}

int main()
{
    FILE *INPUT;
    int n, i;

    INPUT = fopen("input.dat", "r");
    if (INPUT == NULL)
    {
        printf("Unable to open input.dat\n");
        return 1;
    }

    printf("Enter the no of states: ");
    scanf("%d", &n);
    printf("Enter the states: ");
    for (i = 0; i < n; i++)
    {
        scanf("%s", states[i]);
    }
    for (i = 0; i < n; i++)
    {
        epsilon_closure(states[i], INPUT);
    }
    fclose(INPUT);
    return 0;
}"""
}

def get_program_code_for_latex(path):
    normalized = path.replace("\\", "/")
    if normalized in FORMATTED_CODE_FOR_LATEX:
        return FORMATTED_CODE_FOR_LATEX[normalized]
    return read_file(path)


# Definition of all 16 experiments
experiments = [
    {
        "num": 1,
        "name": "Design and Implement a Lexical Analyzer using C Language",
        "programs": [
            ("C Program (lexical_analyzer.c)", "01_Lexical_Analyzer_in_C/lexical_analyzer.c")
        ],
        "input_files": [
            ("input.dat", "01_Lexical_Analyzer_in_C/input.dat")
        ],
        "clearpage_output": True,
        "io": """int is keyword
= is special character
a is identifier
; is special character
10 is constant
float is keyword
= is special character
b is identifier
+ is special character
a is identifier
; is special character
20 is constant
( is special character
if is keyword
b is identifier
) is special character
30 is constant
{ is special character
return is keyword
; is special character
b is identifier
} is special character"""
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
        "input_files": [
            ("input.dat", "09_Epsilon_Closure/input.dat")
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
Continue(0/1)? 0""",
        "clearpage_output": True
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
        code = get_program_code_for_latex(filepath)
        tex_content.append("\\begin{lstlisting}\n")
        tex_content.append(code.rstrip())
        tex_content.append("\n\\end{lstlisting}\n\n")
    else:
        for title, filepath in exp["programs"]:
            code = get_program_code_for_latex(filepath)
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
    if "input_files" in exp:
        for title, filepath in exp["input_files"]:
            content = read_file(filepath)
            tex_content.append(f"\\noindent\\textbf{{{title}:}}\\par\\vspace{{0.2em}}\n")
            tex_content.append("\\begin{lstlisting}\n")
            tex_content.append(content.rstrip())
            tex_content.append("\n\\end{lstlisting}\n\\vspace{0.4em}\n")
        tex_content.append("\\noindent\\textbf{Output:}\\par\\vspace{0.2em}\n")
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
