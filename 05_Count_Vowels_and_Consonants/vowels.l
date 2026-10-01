%{
#include <stdio.h>
int v = 0;
int c = 0;
%}

%%
[aeiouAEIOU] { v++; }
[a-zA-Z]     { c++; }
[ \t\n]      ;
.            ;
%%

int main() {
    printf("Enter string: ");
    yylex();
    printf("Vowels: %d\n", v);
    printf("Consonants: %d\n", c);
    return 0;
}

int yywrap() {
    return 1;
}
