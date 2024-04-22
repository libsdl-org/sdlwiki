###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

* [SDL_GetKeyboardState](SDL_GetKeyboardState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

