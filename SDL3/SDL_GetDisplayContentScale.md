###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetDisplayContentScale

Get the content scale of a display.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
float SDL_GetDisplayContentScale(SDL_DisplayID displayID);
```

## Function Parameters

|                                |               |                                          |
| ------------------------------ | ------------- | ---------------------------------------- |
| [SDL_DisplayID](SDL_DisplayID) | **displayID** | the instance ID of the display to query. |

## Return Value

(float) Returns the content scale of the display, or 0.0f on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The content scale is the expected scale for content based on the DPI
settings of the display. For example, a 4K display might have a 2.0 (200%)
display scale, which means that the user expects UI elements to be twice as
big on this display, to aid in readability.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

