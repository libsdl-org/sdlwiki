
CC = gcc                  # Variable représentant le nom du compilateur.
CFLAGS = -Wall -I include # Variable représentant les options de compilation.
LDFLAGS = -L lib -lZDS    # Variable représentant les options d’édition de liens. 


Programme : main.o        # Programme dépend de `main.o`.
    $(CC) main.o -o Programme $(LDFLAGS)

main.o : src/main.c       # `main.o` dépend de `src/main.c`.
    $(CC) $(CFLAGS) -c src/main.c -o main.o