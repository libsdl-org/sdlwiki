###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowOpacity

Get the opacity of a window.

## Syntax

```c
int SDL_GetWindowOpacity(SDL_Window * window, float * out_opacity);

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

This function is available since SDL 2.0.5.

## Related Functions

* [SDL_SetWindowOpacity](SDL_SetWindowOpacity)

----
[CategoryAPI](CategoryAPI)

