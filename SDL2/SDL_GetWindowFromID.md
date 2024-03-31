###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowFromID

Get a window from a stored ID.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_Window * SDL_GetWindowFromID(Uint32 id);

```

## Function Parameters

|            |                      |
| ---------- | -------------------- |
| **id**     | the ID of the window |

## Return Value

Returns the window associated with `id` or NULL if it doesn't exist; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The numeric ID is what [SDL_WindowEvent](SDL_WindowEvent) references, and
is necessary to map these events to specific [SDL_Window](SDL_Window)
objects.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowID](SDL_GetWindowID)

----
[CategoryAPI](CategoryAPI)

