###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetKeymapScancode

Get the scancode and modifier state corresponding to the given key code using the provided keymap.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Scancode SDL_GetKeymapScancode(SDL_Keymap *keymap, SDL_Keycode keycode, SDL_Keymod *modstate);
```

## Function Parameters

|                            |              |                                                                                                       |
| -------------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| [SDL_Keymap](SDL_Keymap) * | **keymap**   | the [SDL_Keymap](SDL_Keymap) to query, or NULL for the default keymap.                                |
| [SDL_Keycode](SDL_Keycode) | **keycode**  | the [SDL_Keycode](SDL_Keycode) to translate.                                                          |
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

- [SDL_GetCurrentKeymap](SDL_GetCurrentKeymap)
- [SDL_GetKeymapKeycode](SDL_GetKeymapKeycode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

