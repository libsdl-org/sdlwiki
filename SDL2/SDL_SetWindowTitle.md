# SDL_SetWindowTitle

Set the title of a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_SetWindowTitle(SDL_Window * window,
                        const char *title);
```

## Function Parameters

|                            |            |                                           |
| -------------------------- | ---------- | ----------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to change.                     |
| const char *               | **title**  | the desired window title in UTF-8 format. |

## Remarks

This string is expected to be in UTF-8 encoding.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetWindowTitle](SDL_GetWindowTitle)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

