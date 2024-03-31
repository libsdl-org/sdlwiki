###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ClearError

Clear any previous error message for this thread.

## Header File

Defined in [SDL_error.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_error.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_ClearError(void);

```

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetError](SDL_GetError)
* [SDL_SetError](SDL_SetError)

----
[CategoryAPI](CategoryAPI), [CategoryError](CategoryError)


