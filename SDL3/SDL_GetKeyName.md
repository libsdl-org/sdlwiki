###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_GetKeyName

Get a human-readable name for a key.

## Syntax

```c
const char* SDL_GetKeyName(SDL_Keycode key);

```

## Function Parameters

|             |                                                 |
| ----------- | ----------------------------------------------- |
| **key**     | the desired [SDL_Keycode](SDL_Keycode.md) to query |

## Return Value

Returns a pointer to a UTF-8 string that stays valid at least until the
next call to this function. If you need it around any longer, you must copy
it. If the key doesn't have a name, this function returns an empty string
("").

## Remarks

See [SDL_Scancode](SDL_Scancode.md) and [SDL_Keycode](SDL_Keycode.md) for
details.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetKeyFromName](SDL_GetKeyFromName.md)
* [SDL_GetKeyFromScancode](SDL_GetKeyFromScancode.md)
* [SDL_GetScancodeFromKey](SDL_GetScancodeFromKey.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryKeyboard](CategoryKeyboard.md), [CategoryDraft](CategoryDraft.md)
