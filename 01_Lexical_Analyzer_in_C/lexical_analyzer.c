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

    int i;

    for (i = 0; i < 10; i++)
    {
        if (strcmp(word, keywords[i]) == 0)
            return 1;
    }

    return 0;
}

int main()
{
    FILE *fp;
    char ch;
    char word[30];
    int i = 0;

    fp = fopen("sample_input.c", "r");

    if (fp == NULL)
    {
        printf("File not found\n");
        return 1;
    }

    printf("Tokens:\n\n");

    while ((ch = fgetc(fp)) != EOF)
    {
        /* Identifier, keyword or constant */
        if (isalnum(ch) || ch == '_')
        {
            word[i] = ch;
            i++;
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

            /* Operators */
            if (ch == '+' || ch == '-' || ch == '*' ||
                ch == '/' || ch == '%' || ch == '=')
            {
                printf("%c : Operator\n", ch);
            }

            /* Delimiters */
            else if (ch == ';' || ch == ',' ||
                     ch == '(' || ch == ')' ||
                     ch == '{' || ch == '}')
            {
                printf("%c : Delimiter\n", ch);
            }
        }
    }

    /* Process last word */
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

    fclose(fp);

    return 0;
}