###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowOpacity

Set the opacity for a window.

## Syntax

```c
int SDL_SetWindowOpacity(SDL_Window * window, float opacity);

```

## Function Parameters

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **window**      | the window which will be made transparent or opaque   |
| **opacity**     | the opacity value (0.0f - transparent, 1.0f - opaque) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The parameter `opacity` will be clamped internally between 0.0f
(transparent) and 1.0f (opaque).

This function also returns -1 if setting the opacity isn't supported.

## Version

This function is available since SDL 2.0.5.

## Related Functions

* [SDL_GetWindowOpacity](SDL_GetWindowOpacity.md)

----
[CategoryAPI](CategoryAPI.md)
