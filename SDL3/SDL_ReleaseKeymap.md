###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReleaseKeymap

Release a reference to the current keyboard layout.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
void SDL_ReleaseKeymap(SDL_Keymap *keymap);
```

## Function Parameters

|                            |            |                                                       |
| -------------------------- | ---------- | ----------------------------------------------------- |
| [SDL_Keymap](SDL_Keymap) * | **keymap** | the [SDL_Keymap](SDL_Keymap) to release, may be NULL. |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetCurrentKeymap](SDL_GetCurrentKeymap)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

