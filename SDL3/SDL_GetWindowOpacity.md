###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetWindowOpacity

Get the opacity of a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
float SDL_GetWindowOpacity(SDL_Window *window);
```

## Function Parameters

|                            |            |                                                   |
| -------------------------- | ---------- | ------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to get the current opacity value from. |

## Return Value

(float) Returns the opacity, (0.0f - transparent, 1.0f - opaque), or -1.0f
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

If transparency isn't supported on this platform, opacity will be returned
as 1.0f without error.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetWindowOpacity](SDL_SetWindowOpacity)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

