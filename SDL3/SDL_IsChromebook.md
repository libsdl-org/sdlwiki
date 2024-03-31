###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IsChromebook

Query if the application is running on a Chromebook.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_bool SDL_IsChromebook(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if this is a Chromebook,
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

