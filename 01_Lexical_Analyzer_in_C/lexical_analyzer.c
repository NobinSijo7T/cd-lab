#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isKeyword(char word[])
{
    char keywords[][10] = {
        "int", "float", "char", "double",
        "if", "else", "for", "while",
        "return", "void"
    };

    for (int i = 0; i < 10; i++)
    {
        if (strcmp(word, keywords[i]) == 0)
            return 1;
    }

    return 0;
}

int main()
{
    char ch;
    char word[30];
    int i = 0;

    printf("Enter the input string:\n");

    while ((ch = getchar()) != '\n' && ch != EOF)
    {
        if (isalnum(ch) || ch == '_')
        {
            word[i++] = ch;
        }
        else
        {
            if (i != 0)
            {
                word[i] = '\0';

                if (isKeyword(word))
                    printf("%s : Keyword\n", word);
                else if (isdigit(word[0]))
                    printf("%s : Constant\n", word);
                else
                    printf("%s : Identifier\n", word);

                i = 0;
            }

            if (ch == '+' || ch == '-' || ch == '*' ||
                ch == '/' || ch == '%' || ch == '=')
            {
                printf("%c : Operator\n", ch);
            }
            else if (ch == ';' || ch == ',' ||
                     ch == '(' || ch == ')' ||
                     ch == '{' || ch == '}')
            {
                printf("%c : Delimiter\n", ch);
            }
        }
    }

    if (i != 0)
    {
        word[i] = '\0';

        if (isKeyword(word))
            printf("%s : Keyword\n", word);
        else if (isdigit(word[0]))
            printf("%s : Constant\n", word);
        else
            printf("%s : Identifier\n", word);
    }

    return 0;
}