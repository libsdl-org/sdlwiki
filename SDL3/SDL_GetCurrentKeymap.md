###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentKeymap

Get a reference to the current keyboard layout.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Keymap * SDL_GetCurrentKeymap(void);
```

## Return Value

([SDL_Keymap](SDL_Keymap) *) Returns the current keymap, or NULL if the
default US-QWERTY keymap is being used.

## Remarks

You should release the reference to the keymap with
[SDL_ReleaseKeymap](SDL_ReleaseKeymap)() when you're done with it.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetKeymapKeycode](SDL_GetKeymapKeycode)
- [SDL_GetKeymapScancode](SDL_GetKeymapScancode)
- [SDL_ReleaseKeymap](SDL_ReleaseKeymap)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

