###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Error

[SDL_Error](SDL_Error)() 

## Header File

Defined in [SDL_error.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_Error(SDL_errorcode code);

```

## Function Parameters

|              |            |
| ------------ | ---------- |
| **code**     | Error code |

## Return Value

Returns unconditionally -1.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

