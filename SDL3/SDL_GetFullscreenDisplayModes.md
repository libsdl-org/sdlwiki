###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetFullscreenDisplayModes

Get a list of fullscreen display modes available on a display.

## Syntax

```c
extern DECLSPEC const SDL_DisplayMode **SDLCALL SDL_GetFullscreenDisplayModes(SDL_DisplayID displayID, int *count);

```

## Function Parameters

|                   |                                                          |
| ----------------- | -------------------------------------------------------- |
| **displayID**     | the instance ID of the display to query                  |
| **count**         | a pointer filled in with the number of displays returned |

## Return Value

Returns a NULL terminated array of display mode pointers which should be
freed with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Remarks

The display modes are sorted in this priority:

- w -> largest to smallest
- h -> largest to smallest
- bits per pixel -> more colors to fewer colors
- packed pixel layout -> largest to smallest
- refresh rate -> highest to lowest
- pixel density -> lowest to highest

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI)

