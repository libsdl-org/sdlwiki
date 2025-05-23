# SDL_SetWindowProgressValue

Sets the value of the progress bar for the given window’s taskbar icon.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_SetWindowProgressValue(SDL_Window *window, float value);
```

## Function Parameters

|                            |            |                                                                                                             |
| -------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window whose progress value is to be modified.                                                          |
| float                      | **value**  | the progress value in the range of [0.0f - 1.0f]. If the value is outside the valid range, it gets clamped. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

