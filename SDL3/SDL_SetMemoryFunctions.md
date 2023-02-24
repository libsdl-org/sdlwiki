###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetMemoryFunctions

Replace SDL's memory allocation functions with a custom set 

## Syntax

```c
int SDL_SetMemoryFunctions(SDL_malloc_func malloc_func,
                           SDL_calloc_func calloc_func,
                           SDL_realloc_func realloc_func,
                           SDL_free_func free_func);

```

## Function Parameters

|                      |                         |
| -------------------- | ----------------------- |
| **malloc_func**      | custom malloc function  |
| **calloc_func**      | custom calloc function  |
| **realloc_func**     | custom realloc function |
| **free_func**        | custom free function    |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

