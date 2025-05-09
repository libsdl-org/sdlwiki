# SDL_ResetKeyboard

Clear the state of the keyboard

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h)

## Syntax

```c
void SDL_ResetKeyboard(void);
```

## Remarks

This function will generate key up events for all pressed keys.

## Version

This function is available since SDL 2.24.0.

## See Also

- [SDL_GetKeyboardState](SDL_GetKeyboardState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

