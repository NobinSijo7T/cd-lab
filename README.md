# Compiler Design Lab (C / Lex / Yacc)

A comprehensive repository containing implementations, test cases, and lab record documentation for the **Compiler Design Laboratory**.

---

## 📑 Lab Record Document

The full compiled lab record document is available in this repository:
- 📄 **[Compiler_Design_Lab_Record.pdf](Compiler_Design_Lab_Record.pdf)**
- 📝 Generated via `build_latex.py` and `Compiler_Design_Lab_Record.tex`

---

## 📂 List of Experiments

| No. | Experiment Name | Implementation Details | Language / Tool |
|:---:|:---|:---|:---:|
| **01** | [Lexical Analyzer in C](01_Lexical_Analyzer_in_C/) | Tokenizes keywords, identifiers, operators, and constants from source code | C |
| **02** | [Lexical Analyzer using Lex](02_Lexical_Analyzer_using_Lex/) | Tokenizer using regular expressions in Flex | Lex / Flex |
| **03** | [Count Lines, Words & Characters](03_Count_Lines_Words_Characters/) | Text analysis and metrics counting | Lex / Flex |
| **04** | [Replace Substring ('abc' to 'ABC')](04_Replace_Substring_abc_to_ABC/) | Pattern matching and string replacement | Lex / Flex |
| **05** | [Count Vowels and Consonants](05_Count_Vowels_and_Consonants/) | Character classification and counting | Lex / Flex |
| **06** | [Validation of Arithmetic Expression](06_Valid_Arithmetic_Expression_YACC/) | Syntax analysis using CFG rules | Lex & YACC (Bison) |
| **07** | [Validation of Identifier](07_Valid_Identifier_YACC/) | Identifier syntax validator | Lex & YACC (Bison) |
| **08** | [Calculator using Lex and YACC](08_Calculator_using_Lex_and_YACC/) | Arithmetic expression evaluator with precedence handling | Lex & YACC (Bison) |
| **09** | [ε-Closure of States in ε-NFA](09_Epsilon_Closure/) | Graph traversal to compute epsilon closures from transition table | C |
| **10** | [Conversion of ε-NFA to DFA](10_NFA_to_DFA/) | Subset construction algorithm for state transition conversion | C |
| **11** | [Minimization of DFA](11_DFA_Minimization/) | State partitioning algorithm (Hopcroft / Table-filling) | C |
| **12** | [Computation of FIRST and FOLLOW](12_First_and_Follow/) | Context-free grammar nullability, FIRST, and FOLLOW set computation | C |
| **13** | [Recursive Descent Parser](13_Recursive_Descent_Parser/) | Top-down predictive parsing via recursive functions | C |
| **14** | [Shift-Reduce Parser](14_Shift_Reduce_Parser/) | Bottom-up parsing using an explicit stack | C |
| **15** | [Constant Propagation](15_Constant_Propagation/) | Machine-independent code optimization | C |
| **16** | [Intermediate Code Generation (ICG)](16_Intermediate_Code_Generation/) | Generation of Three-Address Code (TAC) from expressions | C |

---

## 🛠️ Compilation & Execution Guide

### 1. Pure C Programs
```bash
gcc program_name.c -o output
./output
```

### 2. Lex / Flex Programs
```bash
flex program.l
gcc lex.yy.c -o output
./output
```

### 3. Lex & YACC (Bison) Programs
```bash
bison -d parser.y
flex lexer.l
gcc y.tab.c lex.yy.c -o output
./output
```

### 4. Building the Lab Record PDF
```bash
python build_latex.py
```
*(Requires `pdflatex` or a TeX distribution like MiKTeX / TeX Live)*
