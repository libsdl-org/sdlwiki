###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDefaultKeyFromScancode

Get the key code corresponding to the given scancode according to a default en_US keyboard layout.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Keycode SDL_GetDefaultKeyFromScancode(SDL_Scancode scancode, SDL_Keymod modstate);
```

## Function Parameters

|                              |              |                                                                       |
| ---------------------------- | ------------ | --------------------------------------------------------------------- |
| [SDL_Scancode](SDL_Scancode) | **scancode** | the desired [SDL_Scancode](SDL_Scancode) to query.                    |
| [SDL_Keymod](SDL_Keymod)     | **modstate** | the modifier state to use when translating the scancode to a keycode. |

## Return Value

([SDL_Keycode](SDL_Keycode)) Returns the [SDL_Keycode](SDL_Keycode) that
corresponds to the given [SDL_Scancode](SDL_Scancode).

## Remarks

See [SDL_Keycode](SDL_Keycode) for details.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetKeyName](SDL_GetKeyName)
- [SDL_GetScancodeFromKey](SDL_GetScancodeFromKey)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

