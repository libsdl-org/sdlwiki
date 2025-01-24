# SDL_ClearComposition

Dismiss the composition window/IME without disabling the subsystem.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
bool SDL_ClearComposition(SDL_Window *window);
```

## Function Parameters

|                            |            |                       |
| -------------------------- | ---------- | --------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to affect. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_StartTextInput](SDL_StartTextInput)
- [SDL_StopTextInput](SDL_StopTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

