###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetWindowTitle

Set the title of a window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowTitle(SDL_Window *window, const char *title);
```

## Function Parameters

|                            |            |                                           |
| -------------------------- | ---------- | ----------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to change.                     |
| const char *               | **title**  | the desired window title in UTF-8 format. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This string is expected to be in UTF-8 encoding.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetWindowTitle](SDL_GetWindowTitle)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

