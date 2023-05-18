###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowPixelDensity

Get the pixel density of a window.

## Syntax

```c
float SDL_GetWindowPixelDensity(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the pixel density or 0.0f on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is a ratio of pixel size to window size. For example, if the window is
1920x1080 and it has a high density back buffer of 3840x2160 pixels, it
would have a pixel density of 2.0.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowDisplayScale](SDL_GetWindowDisplayScale)

----
[CategoryAPI](CategoryAPI)

