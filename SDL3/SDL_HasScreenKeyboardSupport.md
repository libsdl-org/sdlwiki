# SDL_HasScreenKeyboardSupport

Check whether the platform has screen keyboard support.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
bool SDL_HasScreenKeyboardSupport(void);
```

## Return Value

(bool) Returns true if the platform has some screen keyboard support or
false if not.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_StartTextInput](SDL_StartTextInput)
- [SDL_ScreenKeyboardShown](SDL_ScreenKeyboardShown)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

