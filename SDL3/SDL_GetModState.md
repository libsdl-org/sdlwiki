# SDL_GetModState

Get the current key modifier state for the keyboard.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Keymod SDL_GetModState(void);
```

## Return Value

([SDL_Keymod](SDL_Keymod)) Returns an OR'd combination of the modifier keys
for the keyboard. See [SDL_Keymod](SDL_Keymod) for details.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetKeyboardState](SDL_GetKeyboardState)
- [SDL_SetModState](SDL_SetModState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

