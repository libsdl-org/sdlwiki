# SDL_GetWindowProgressValue

Get the value of the progress bar for the given window’s taskbar icon.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
float SDL_GetWindowProgressValue(SDL_Window *window);
```

## Function Parameters

|                            |            |                                                    |
| -------------------------- | ---------- | -------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to get the current progress value from. |

## Return Value

(float) Returns the progress value in the range of [0.0f - 1.0f], or -1.0f
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

