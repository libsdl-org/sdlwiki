###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetNumDisplayModes

Get the number of available display modes.

## Syntax

```c
int SDL_GetNumDisplayModes(int displayIndex);

```

## Function Parameters

|                      |                                   |
| -------------------- | --------------------------------- |
| **displayIndex**     | the index of the display to query |

## Return Value

Returns a number >= 1 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The `displayIndex` needs to be in the range from 0 to
[SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays.md)() - 1.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetDisplayMode](SDL_GetDisplayMode.md)
* [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays.md)

----
[CategoryAPI](CategoryAPI.md)
