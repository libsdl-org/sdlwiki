###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWsize

Use this function to get the size of the data stream in an [SDL_RWops](SDL_RWops).

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
Sint64 SDL_RWsize(SDL_RWops *context);

```

## Function Parameters

|                 |                                                                    |
| --------------- | ------------------------------------------------------------------ |
| **context**     | the [SDL_RWops](SDL_RWops) to get the size of the data stream from |

## Return Value

Returns the size of the data stream in the [SDL_RWops](SDL_RWops) on
success, -1 if unknown or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Prior to SDL 2.0.10, this function was a macro.

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

