###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowGrab

Get a window's input grab mode.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
SDL_bool SDL_GetWindowGrab(SDL_Window * window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if input is grabbed, [SDL_FALSE](SDL_FALSE)
otherwise.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SetWindowGrab](SDL_SetWindowGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

