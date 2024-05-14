###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowOpacity

Get the opacity of a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
int SDL_GetWindowOpacity(SDL_Window *window, float *out_opacity);

```

## Function Parameters

|                     |                                                         |
| ------------------- | ------------------------------------------------------- |
| **window**          | the window to get the current opacity value from        |
| **out_opacity**     | the float filled in (0.0f - transparent, 1.0f - opaque) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If transparency isn't supported on this platform, opacity will be reported
as 1.0f without error.

The parameter `opacity` is ignored if it is NULL.

This function also returns -1 if an invalid window was provided.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetWindowOpacity](SDL_SetWindowOpacity)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

