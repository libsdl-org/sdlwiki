###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_StopTextInput

Stop receiving any text input events in a window.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
bool SDL_StopTextInput(SDL_Window *window);
```

## Function Parameters

|                            |            |                                   |
| -------------------------- | ---------- | --------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to disable text input. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If [SDL_StartTextInput](SDL_StartTextInput)() showed the screen keyboard,
this function will hide it.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_StartTextInput](SDL_StartTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

