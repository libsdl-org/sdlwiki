###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDefaultScancodeFromKey

Get the scancode corresponding to the given key code according to a default en_US keyboard layout.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Scancode SDL_GetDefaultScancodeFromKey(SDL_Keycode key, SDL_Keymod *modstate);
```

## Function Parameters

|                            |              |                                                                                                       |
| -------------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| [SDL_Keycode](SDL_Keycode) | **key**      | the desired [SDL_Keycode](SDL_Keycode) to query.                                                      |
| [SDL_Keymod](SDL_Keymod) * | **modstate** | a pointer to the modifier state that would be used when the scancode generates this key, may be NULL. |

## Return Value

([SDL_Scancode](SDL_Scancode)) Returns the [SDL_Scancode](SDL_Scancode)
that corresponds to the given [SDL_Keycode](SDL_Keycode).

## Remarks

Note that there may be multiple scancode+modifier states that can generate
this keycode, this will just return the first one found.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetScancodeFromKey](SDL_GetScancodeFromKey)
- [SDL_GetScancodeName](SDL_GetScancodeName)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

