#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int isKeyword(char buffer[])
{
    char keyword[32][10] = {
        "auto", "break", "case", "char", "const",
        "continue", "default", "do", "double", "else",
        "enum", "extern", "float", "for", "goto",
        "if", "int", "long", "register", "return",
        "short", "signed", "sizeof", "static", "struct",
        "switch", "typedef", "union", "unsigned", "void",
        "volatile", "while"
    };

    int i;

    for (i = 0; i < 32; i++)
    {
        if (strcmp(keyword[i], buffer) == 0)
            return 1;
    }

    return 0;
}

int main()
{
    char ch;
    char buffer[50];

    char operators[] = "+-*/%=";
    char specialch[] = ";,(){}";

    FILE *fp;
    int i, j = 0;

    fp = fopen("input.dat", "r");
    if (fp == NULL)
    {
        fp = fopen("program.txt", "r");
    }

    if (fp == NULL)
    {
        printf("Error opening file\n");
        exit(0);
    }

    while ((ch = fgetc(fp)) != EOF)
    {
        /* Check operators */
        for (i = 0; i < 6; i++)
        {
            if (ch == operators[i])
            {
                printf("%c is special character\n", ch);
                break;
            }
        }

        /* Check special characters */
        for (i = 0; i < 6; i++)
        {
            if (ch == specialch[i])
            {
                printf("%c is special character\n", ch);
                break;
            }
        }

        /* Build a word or number */
        if (isalnum(ch))
        {
            buffer[j++] = ch;
        }
        else if (j != 0)
        {
            buffer[j] = '\0';
            j = 0;

            /* Check whether token is a keyword */
            if (isKeyword(buffer))
            {
                printf("%s is keyword\n", buffer);
            }
            /* Check whether token is a number */
            else if (isdigit(buffer[0]))
            {
                int flag = 1;

                for (i = 0; buffer[i] != '\0'; i++)
                {
                    if (!isdigit(buffer[i]))
                    {
                        flag = 0;
                        break;
                    }
                }

                if (flag)
                    printf("%s is constant\n", buffer);
                else
                    printf("%s is identifier\n", buffer);
            }
            else
            {
                printf("%s is identifier\n", buffer);
            }
        }
    }

    /* Process last token if file doesn't end with whitespace */
    if (j != 0)
    {
        buffer[j] = '\0';

        if (isKeyword(buffer))
        {
            printf("%s is keyword\n", buffer);
        }
        else if (isdigit(buffer[0]))
        {
            printf("%s is constant\n", buffer);
        }
        else
        {
            printf("%s is identifier\n", buffer);
        }
    }

    fclose(fp);

    return 0;
}