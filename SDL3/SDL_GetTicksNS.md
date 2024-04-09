###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTicksNS

Get the number of nanoseconds since SDL library initialization.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
Uint64 SDL_GetTicksNS(void);

```

## Return Value

Returns an unsigned 64-bit value representing the number of nanoseconds
since the SDL library initialized.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

