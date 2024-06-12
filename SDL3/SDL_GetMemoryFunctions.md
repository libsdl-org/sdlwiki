###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetMemoryFunctions

Get the current set of SDL memory functions.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_GetMemoryFunctions(SDL_malloc_func *malloc_func,
                        SDL_calloc_func *calloc_func,
                        SDL_realloc_func *realloc_func,
                        SDL_free_func *free_func);
```

## Function Parameters

|                                        |                  |                              |
| -------------------------------------- | ---------------- | ---------------------------- |
| [SDL_malloc_func](SDL_malloc_func) *   | **malloc_func**  | filled with malloc function  |
| [SDL_calloc_func](SDL_calloc_func) *   | **calloc_func**  | filled with calloc function  |
| [SDL_realloc_func](SDL_realloc_func) * | **realloc_func** | filled with realloc function |
| [SDL_free_func](SDL_free_func) *       | **free_func**    | filled with free function    |

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

