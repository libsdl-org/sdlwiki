###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_StartTextInput

Start accepting Unicode text input events in a window.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
int SDL_StartTextInput(SDL_Window *window);
```

## Function Parameters

|                            |            |                                  |
| -------------------------- | ---------- | -------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to enable text input. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function will enable text input
([SDL_EVENT_TEXT_INPUT](SDL_EVENT_TEXT_INPUT) and
[SDL_EVENT_TEXT_EDITING](SDL_EVENT_TEXT_EDITING) events) in the specified
window. Please use this function paired with
[SDL_StopTextInput](SDL_StopTextInput)().

Text input events are not received by default.

On some platforms using this function shows the screen keyboard.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetTextInputArea](SDL_SetTextInputArea)
- [SDL_StopTextInput](SDL_StopTextInput)
- [SDL_TextInputActive](SDL_TextInputActive)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

