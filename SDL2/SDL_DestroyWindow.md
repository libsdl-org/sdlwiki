###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyWindow

Destroy a window.

## Syntax

```c
void SDL_DestroyWindow(SDL_Window * window);

```

## Function Parameters

|                |                       |
| -------------- | --------------------- |
| **window**     | the window to destroy |

## Remarks

If `window` is NULL, this function will return immediately after setting
the SDL error message to "Invalid window". See
[SDL_GetError](SDL_GetError.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateWindow](SDL_CreateWindow.md)
* [SDL_CreateWindowFrom](SDL_CreateWindowFrom.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
