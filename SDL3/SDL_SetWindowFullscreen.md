###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowFullscreen

Set a window's fullscreen state.

## Syntax

```c
int SDL_SetWindowFullscreen(SDL_Window *window, SDL_bool fullscreen);

```

## Function Parameters

|                    |                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------- |
| **window**         | the window to change                                                               |
| **fullscreen**     | [SDL_TRUE](SDL_TRUE) for fullscreen mode, [SDL_FALSE](SDL_FALSE) for windowed mode |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

By default a window in fullscreen state uses fullscreen desktop mode, but a
specific display mode can be set using
[SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowFullscreenMode](SDL_GetWindowFullscreenMode)
* [SDL_SetWindowFullscreenMode](SDL_SetWindowFullscreenMode)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


