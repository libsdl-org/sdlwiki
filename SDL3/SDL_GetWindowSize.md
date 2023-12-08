###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowSize

Get the size of a window's client area.

## Syntax

```c
int SDL_GetWindowSize(SDL_Window *window, int *w, int *h);

```

## Function Parameters

|                |                                                                |
| -------------- | -------------------------------------------------------------- |
| **window**     | the window to query the width and height from                  |
| **w**          | a pointer filled in with the width of the window, may be NULL  |
| **h**          | a pointer filled in with the height of the window, may be NULL |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

NULL can safely be passed as the `w` or `h` parameter if the width or
height value is not desired.

The window pixel size may differ from its window coordinate size if the
window is on a high pixel density display. Use
[SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels.md)() or
[SDL_GetRenderOutputSize](SDL_GetRenderOutputSize.md)() to get the real client
area size in pixels.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderOutputSize](SDL_GetRenderOutputSize.md)
* [SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels.md)
* [SDL_SetWindowSize](SDL_SetWindowSize.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
