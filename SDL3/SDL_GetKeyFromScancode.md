###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetKeyFromScancode

Get the key code corresponding to the given scancode according to the current keyboard layout.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Keycode SDL_GetKeyFromScancode(SDL_Scancode scancode, SDL_Keymod modstate, bool key_event);
```

## Function Parameters

|                              |               |                                                                       |
| ---------------------------- | ------------- | --------------------------------------------------------------------- |
| [SDL_Scancode](SDL_Scancode) | **scancode**  | the desired [SDL_Scancode](SDL_Scancode) to query.                    |
| [SDL_Keymod](SDL_Keymod)     | **modstate**  | the modifier state to use when translating the scancode to a keycode. |
| bool                         | **key_event** | true if the keycode will be used in key events.                       |

## Return Value

([SDL_Keycode](SDL_Keycode)) Returns the [SDL_Keycode](SDL_Keycode) that
corresponds to the given [SDL_Scancode](SDL_Scancode).

## Remarks

If you want to get the keycode as it would be delivered in key events,
including options specified in
[SDL_HINT_KEYCODE_OPTIONS](SDL_HINT_KEYCODE_OPTIONS), then you should pass
`key_event` as true. Otherwise this function simply translates the scancode
based on the given modifier state.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetKeyName](SDL_GetKeyName)
- [SDL_GetScancodeFromKey](SDL_GetScancodeFromKey)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

