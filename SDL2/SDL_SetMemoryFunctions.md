# SDL_SetMemoryFunctions

Replace SDL's memory allocation functions with a custom set

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h)

## Syntax

```c
int SDL_SetMemoryFunctions(SDL_malloc_func malloc_func,
                           SDL_calloc_func calloc_func,
                           SDL_realloc_func realloc_func,
                           SDL_free_func free_func);
```

## Function Parameters

|                                      |                  |                          |
| ------------------------------------ | ---------------- | ------------------------ |
| [SDL_malloc_func](SDL_malloc_func)   | **malloc_func**  | custom malloc function.  |
| [SDL_calloc_func](SDL_calloc_func)   | **calloc_func**  | custom calloc function.  |
| [SDL_realloc_func](SDL_realloc_func) | **realloc_func** | custom realloc function. |
| [SDL_free_func](SDL_free_func)       | **free_func**    | custom free function.    |

## Return Value

(int) Returns 0 on success or -1 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.7.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdInc](CategoryStdInc)

