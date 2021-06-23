#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - runs an infinite loop for testing
 *
 * Return: always 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
/**
 * main - entry point for program
 *
 * Return: always 0
 */
int main(void) {
    int cntr, id;

    for (cntr=0; cntr<5; ++cntr) {
        id = fork();
        if (id < 0) {
            continue;
        }
        
        else if (id == 0) {
            exit(0);
        } else {
            printf("Zombie process created, PID: %d\n", id);
        }        
    }
    infinite_while();
    return (0);
}
