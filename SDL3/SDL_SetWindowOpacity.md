# SDL_SetWindowOpacity

Set the opacity for a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowOpacity(SDL_Window *window, float opacity);
```

## Function Parameters

|                            |             |                                                        |
| -------------------------- | ----------- | ------------------------------------------------------ |
| [SDL_Window](SDL_Window) * | **window**  | the window which will be made transparent or opaque.   |
| float                      | **opacity** | the opacity value (0.0f - transparent, 1.0f - opaque). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The parameter `opacity` will be clamped internally between 0.0f
(transparent) and 1.0f (opaque).

This function also returns false if setting the opacity isn't supported.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetWindowOpacity](SDL_GetWindowOpacity)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

