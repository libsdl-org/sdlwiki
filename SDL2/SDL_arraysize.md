###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_arraysize

The number of elements in an array.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_arraysize(array)    (sizeof(array)/sizeof(array[0]))
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

