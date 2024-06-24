###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StopTextInput

Stop receiving any text input events in a window.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
int SDL_StopTextInput(SDL_Window *window);
```

## Function Parameters

|                            |            |                                   |
| -------------------------- | ---------- | --------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to disable text input. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If [SDL_StartTextInput](SDL_StartTextInput)() showed the screen keyboard,
this function will hide it.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_StartTextInput](SDL_StartTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

