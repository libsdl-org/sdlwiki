###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetMemoryFunctions

Replace SDL's memory allocation functions with a custom set

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_SetMemoryFunctions(SDL_malloc_func malloc_func,
                           SDL_calloc_func calloc_func,
                           SDL_realloc_func realloc_func,
                           SDL_free_func free_func);

```

## Version

This function is available since SDL 2.0.7.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

