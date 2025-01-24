# SDL_DestroyWindow

Destroy a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
void SDL_DestroyWindow(SDL_Window *window);
```

## Function Parameters

|                            |            |                        |
| -------------------------- | ---------- | ---------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to destroy. |

## Remarks

Any child windows owned by the window will be recursively destroyed as
well.

Note that on some platforms, the visible window may not actually be removed
from the screen until the SDL event loop is pumped again, even though the
[SDL_Window](SDL_Window) is no longer valid after this call.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreatePopupWindow](SDL_CreatePopupWindow)
- [SDL_CreateWindow](SDL_CreateWindow)
- [SDL_CreateWindowWithProperties](SDL_CreateWindowWithProperties)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

