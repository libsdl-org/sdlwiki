# SDL_GetWindowProgressState

Get the state of the progress bar for the given window’s taskbar icon.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_ProgressState SDL_GetWindowProgressState(SDL_Window *window);
```

## Function Parameters

|                            |            |                                                    |
| -------------------------- | ---------- | -------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to get the current progress state from. |

## Return Value

([SDL_ProgressState](SDL_ProgressState)) Returns the progress state, or
[SDL_PROGRESS_STATE_INVALID](SDL_PROGRESS_STATE_INVALID) on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

