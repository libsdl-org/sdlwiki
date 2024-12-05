###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetScancodeFromKey

Get the scancode corresponding to the given key code according to the current keyboard layout.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Scancode SDL_GetScancodeFromKey(SDL_Keycode key, SDL_Keymod *modstate);
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

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetKeyFromScancode](SDL_GetKeyFromScancode)
- [SDL_GetScancodeName](SDL_GetScancodeName)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

