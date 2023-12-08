###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowTitle

Set the title of a window.

## Syntax

```c
void SDL_SetWindowTitle(SDL_Window * window,
                        const char *title);

```

## Function Parameters

|                |                                          |
| -------------- | ---------------------------------------- |
| **window**     | the window to change                     |
| **title**      | the desired window title in UTF-8 format |

## Remarks

This string is expected to be in UTF-8 encoding.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowTitle](SDL_GetWindowTitle.md)

----
[CategoryAPI](CategoryAPI.md)
