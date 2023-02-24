###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowPixelFormat

Get the pixel format associated with the window.

## Syntax

```c
Uint32 SDL_GetWindowPixelFormat(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the pixel format of the window on success or
[SDL_PIXELFORMAT_UNKNOWN](SDL_PIXELFORMAT_UNKNOWN) on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


