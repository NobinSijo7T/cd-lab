#include <stdio.h>
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
            if (strcmp(current, state1) == 0 &&
                strcmp(input, "e") == 0)
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
}

