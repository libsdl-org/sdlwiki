###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetMemoryFunctions

Get the current set of SDL memory functions 

## Syntax

```c
void SDL_GetMemoryFunctions(SDL_malloc_func *malloc_func,
                            SDL_calloc_func *calloc_func,
                            SDL_realloc_func *realloc_func,
                            SDL_free_func *free_func);

```

## Function Parameters

|                      |                              |
| -------------------- | ---------------------------- |
| **malloc_func**      | filled with malloc function  |
| **calloc_func**      | filled with calloc function  |
| **realloc_func**     | filled with realloc function |
| **free_func**        | filled with free function    |

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

