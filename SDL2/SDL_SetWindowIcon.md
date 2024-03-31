###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowIcon

Set the icon for a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_SetWindowIcon(SDL_Window * window,
                       SDL_Surface * icon);

```

## Function Parameters

|                |                                                                            |
| -------------- | -------------------------------------------------------------------------- |
| **window**     | the window to change                                                       |
| **icon**       | an [SDL_Surface](SDL_Surface) structure containing the icon for the window |

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI)

