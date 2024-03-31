###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowSize

Get the size of a window's client area.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h), but apps should _only_ `#include <SDL3/SDL.h>`!

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
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

NULL can safely be passed as the `w` or `h` parameter if the width or
height value is not desired.

The window pixel size may differ from its window coordinate size if the
window is on a high pixel density display. Use
[SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels)() or
[SDL_GetRenderOutputSize](SDL_GetRenderOutputSize)() to get the real client
area size in pixels.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderOutputSize](SDL_GetRenderOutputSize)
* [SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels)
* [SDL_SetWindowSize](SDL_SetWindowSize)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


