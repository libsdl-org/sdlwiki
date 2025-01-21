###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetWindowSizeInPixels

Get the size of a window's client area, in pixels.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_GetWindowSizeInPixels(SDL_Window *window, int *w, int *h);
```

## Function Parameters

|                            |            |                                                                      |
| -------------------------- | ---------- | -------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window from which the drawable size should be queried.           |
| int *                      | **w**      | a pointer to variable for storing the width in pixels, may be NULL.  |
| int *                      | **h**      | a pointer to variable for storing the height in pixels, may be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateWindow](SDL_CreateWindow)
- [SDL_GetWindowSize](SDL_GetWindowSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

