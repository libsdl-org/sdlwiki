###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetKeyFromScancode

Get the key code corresponding to the given scancode according to the current keyboard layout.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_Keycode SDL_GetKeyFromScancode(SDL_Scancode scancode);

```

## Function Parameters

|                  |                                                   |
| ---------------- | ------------------------------------------------- |
| **scancode**     | the desired [SDL_Scancode](SDL_Scancode) to query |

## Return Value

Returns the [SDL_Keycode](SDL_Keycode) that corresponds to the given
[SDL_Scancode](SDL_Scancode).

## Remarks

See [SDL_Keycode](SDL_Keycode) for details.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetKeyName](SDL_GetKeyName)
* [SDL_GetScancodeFromKey](SDL_GetScancodeFromKey)

----
[CategoryAPI](CategoryAPI)

