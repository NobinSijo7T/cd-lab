%{
#include <stdio.h>
int v=0;
int c=0;
%}
%%
[aeiouAEIOU] {c++;}
. {v++;}
%%
int main() {
printf("Enter ip:");
yylex();
printf("consonent: %d", v);
printf("\nvovel: %d", c);
}
int yywrap(){
return 1;
}
