###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetKeyFromName

Get a key code from a human-readable name.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Keycode SDL_GetKeyFromName(const char *name, SDL_bool uppercase);
```

## Function Parameters

|                      |               |                                                                                                                                                                                                                                         |
| -------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| const char *         | **name**      | the human-readable key name.                                                                                                                                                                                                            |
| [SDL_bool](SDL_bool) | **uppercase** | [SDL_TRUE](SDL_TRUE) if the name is the letter printed on the key on the keyboard, which is usually uppercase, and this function should return the unshifted version of the key, or [SDL_FALSE](SDL_FALSE) to return the key unchanged. |

## Return Value

([SDL_Keycode](SDL_Keycode)) Returns key code, or
[`SDLK_UNKNOWN`](SDLK_UNKNOWN) if the name wasn't recognized; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetKeyFromScancode](SDL_GetKeyFromScancode)
- [SDL_GetKeyName](SDL_GetKeyName)
- [SDL_GetScancodeFromName](SDL_GetScancodeFromName)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

