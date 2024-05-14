###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDisplayBounds

Get the desktop area represented by a display.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GetDisplayBounds(int displayIndex, SDL_Rect * rect);

```

## Function Parameters

|                      |                                                                      |
| -------------------- | -------------------------------------------------------------------- |
| **displayIndex**     | the index of the display to query                                    |
| **rect**             | the [SDL_Rect](SDL_Rect) structure filled in with the display bounds |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The primary display (`displayIndex` zero) is always located at 0,0.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

