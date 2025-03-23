# SDL_SetWindowProgressState

Sets the state of the progress bar for the given window’s taskbar icon.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowProgressState(SDL_Window *window, SDL_ProgressState state);
```

## Function Parameters

|                                        |            |                                                                                                             |
| -------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) *             | **window** | the window whose progress state is to be modified.                                                          |
| [SDL_ProgressState](SDL_ProgressState) | **state**  | the progress state. [`SDL_PROGRESS_STATE_NONE`](SDL_PROGRESS_STATE_NONE) stops displaying the progress bar. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

