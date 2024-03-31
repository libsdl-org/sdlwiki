###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetScancodeFromName

Get a scancode from a human-readable name.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_Scancode SDL_GetScancodeFromName(const char *name);

```

## Function Parameters

|              |                                  |
| ------------ | -------------------------------- |
| **name**     | the human-readable scancode name |

## Return Value

Returns the [SDL_Scancode](SDL_Scancode), or
[`SDL_SCANCODE_UNKNOWN`](SDL_SCANCODE_UNKNOWN) if the name wasn't
recognized; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetKeyFromName](SDL_GetKeyFromName)
* [SDL_GetScancodeFromKey](SDL_GetScancodeFromKey)
* [SDL_GetScancodeName](SDL_GetScancodeName)

----
[CategoryAPI](CategoryAPI)

