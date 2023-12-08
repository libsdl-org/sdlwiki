###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyWindow

Destroy a window.

## Syntax

```c
void SDL_DestroyWindow(SDL_Window *window);

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePopupWindow](SDL_CreatePopupWindow.md)
* [SDL_CreateWindow](SDL_CreateWindow.md)
* [SDL_CreateWindowWithProperties](SDL_CreateWindowWithProperties.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
