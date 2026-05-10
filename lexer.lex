%{
#include<stdio.h>
%}

%%

"if"|"else"|"for"|"while"|"def"|"return"|"import"|"class"|"break"|"continue" { printf("Reserved Word : %s\n", yytext); }

[0-9]+(\.[0-9]+)? { printf("Constant : %s\n", yytext); }

\"[^\"]*\" { printf("String Literal : %s\n", yytext); }

"#".* { printf("Comment : %s\n", yytext); }

"=="|"!="|"<="|">="|"+"|"-"|"*"|"/"|"="|"<"|">"|"%" { printf("Operator : %s\n", yytext); }

[\(\)\{\}\[\]:;,.] { printf("Special Symbol : %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]* { printf("Identifier : %s\n", yytext); }

[ \t\n]+ ;

. { printf("Unknown : %s\n", yytext); }

%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();
    return 0;
}
