# SDL_GetOriginalMemoryFunctions

Get the original set of SDL memory functions

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h)

## Syntax

```c
void SDL_GetOriginalMemoryFunctions(SDL_malloc_func *malloc_func,
                                    SDL_calloc_func *calloc_func,
                                    SDL_realloc_func *realloc_func,
                                    SDL_free_func *free_func);
```

## Function Parameters

|                                        |                  |                               |
| -------------------------------------- | ---------------- | ----------------------------- |
| [SDL_malloc_func](SDL_malloc_func) *   | **malloc_func**  | filled with malloc function.  |
| [SDL_calloc_func](SDL_calloc_func) *   | **calloc_func**  | filled with calloc function.  |
| [SDL_realloc_func](SDL_realloc_func) * | **realloc_func** | filled with realloc function. |
| [SDL_free_func](SDL_free_func) *       | **free_func**    | filled with free function.    |

## Version

This function is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdInc](CategoryStdInc)

