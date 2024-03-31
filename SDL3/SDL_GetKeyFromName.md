###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_GetKeyFromName

Get a key code from a human-readable name.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_Keycode SDL_GetKeyFromName(const char *name);

```

## Function Parameters

|              |                             |
| ------------ | --------------------------- |
| **name**     | the human-readable key name |

## Return Value

Returns key code, or [`SDLK_UNKNOWN`](SDLK_UNKNOWN) if the name wasn't
recognized; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetKeyFromScancode](SDL_GetKeyFromScancode)
* [SDL_GetKeyName](SDL_GetKeyName)
* [SDL_GetScancodeFromName](SDL_GetScancodeFromName)

----
[CategoryAPI](CategoryAPI), [CategoryKeyboard](CategoryKeyboard), [CategoryDraft](CategoryDraft)


