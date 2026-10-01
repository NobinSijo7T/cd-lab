%{
#include <stdio.h>
%}

%%
int|float|for|if|else|while { printf("keyword "); }
[a-zA-Z][a-zA-Z0-9]*        { printf("identifier "); }
[0-9]+                      { printf("number "); }
[+\-*/=]                    { printf("operator "); }
[ \t\n]+                    { /* skip whitespace */ }
.                           { /* skip other characters */ }
%%

int main() {
    printf("enter ip: ");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
