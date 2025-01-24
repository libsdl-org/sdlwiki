# SDL_GetMemoryFunctions

Get the current set of SDL memory functions

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h)

## Syntax

```c
void SDL_GetMemoryFunctions(SDL_malloc_func *malloc_func,
                            SDL_calloc_func *calloc_func,
                            SDL_realloc_func *realloc_func,
                            SDL_free_func *free_func);
```

## Version

This function is available since SDL 2.0.7.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdInc](CategoryStdInc)

