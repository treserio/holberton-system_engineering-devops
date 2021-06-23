#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

// requirement after 5 zombies are created
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void) {
    int cntr, id;

    for (cntr=0; cntr<5; ++cntr) {
        id = fork();
        if (id < 0) {
            continue;
        }
        // if parent = 0? seems the thing to do is exit?
        else if (id == 0) {
            exit(0);
        } else {
            printf("Zombie process created, PID: %s\n", id);
        }        
    }
    infinite_while();
    return (0);
}