###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowSize

Set the size of a window's client area.

## Syntax

```c
int SDL_SetWindowSize(SDL_Window *window, int w, int h);

```

## Function Parameters

|                |                                       |
| -------------- | ------------------------------------- |
| **window**     | the window to change                  |
| **w**          | the width of the window, must be > 0  |
| **h**          | the height of the window, must be > 0 |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This only affects the size of the window when not in fullscreen mode. To
change the fullscreen mode of a window, use
[SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)()

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowSize](SDL_GetWindowSize)
* [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


