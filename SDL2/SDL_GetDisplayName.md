###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDisplayName

Get the name of a display in UTF-8 encoding.

## Syntax

```c
const char * SDL_GetDisplayName(int displayIndex);

```

## Function Parameters

|                      |                                                            |
| -------------------- | ---------------------------------------------------------- |
| **displayIndex**     | the index of display from which the name should be queried |

## Return Value

Returns the name of a display or NULL for an invalid display index or
failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays.md)

----
[CategoryAPI](CategoryAPI.md)
