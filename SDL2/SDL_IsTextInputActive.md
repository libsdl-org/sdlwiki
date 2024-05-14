###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsTextInputActive

Check whether or not Unicode text input events are enabled.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h)

## Syntax

```c
SDL_bool SDL_IsTextInputActive(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if text input events are enabled else
[SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_StartTextInput](SDL_StartTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

