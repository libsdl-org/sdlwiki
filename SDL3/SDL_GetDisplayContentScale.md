###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDisplayContentScale

Get the content scale of a display.

## Syntax

```c
float SDL_GetDisplayContentScale(SDL_DisplayID displayID);

```

## Function Parameters

|                   |                                         |
| ----------------- | --------------------------------------- |
| **displayID**     | the instance ID of the display to query |

## Return Value

Returns The content scale of the display, or 0.0f on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Remarks

The content scale is the expected scale for content based on the DPI
settings of the display. For example, a 4K display might have a 2.0 (200%)
display scale, which means that the user expects UI elements to be twice as
big on this display, to aid in readability.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetDisplays](SDL_GetDisplays)

----
[CategoryAPI](CategoryAPI)

