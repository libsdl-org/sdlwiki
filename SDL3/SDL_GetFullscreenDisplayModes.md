###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetFullscreenDisplayModes

Get a list of fullscreen display modes available on a display.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_DisplayMode ** SDL_GetFullscreenDisplayModes(SDL_DisplayID displayID, int *count);
```

## Function Parameters

|                                |               |                                                                             |
| ------------------------------ | ------------- | --------------------------------------------------------------------------- |
| [SDL_DisplayID](SDL_DisplayID) | **displayID** | the instance ID of the display to query.                                    |
| int *                          | **count**     | a pointer filled in with the number of display modes returned, may be NULL. |

## Return Value

([SDL_DisplayMode](SDL_DisplayMode) **) Returns a NULL terminated array of
display mode pointers or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This is a single
allocation that should be freed with [SDL_free](SDL_free)() when it is no
longer needed.

## Remarks

The display modes are sorted in this priority:

- w -> largest to smallest
- h -> largest to smallest
- bits per pixel -> more colors to fewer colors
- packed pixel layout -> largest to smallest
- refresh rate -> highest to lowest
- pixel density -> lowest to highest

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

