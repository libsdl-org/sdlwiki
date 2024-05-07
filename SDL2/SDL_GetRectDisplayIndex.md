###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetRectDisplayIndex

Get the index of the display primarily containing a rect

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GetRectDisplayIndex(const SDL_Rect * rect);

```

## Function Parameters

|              |                   |
| ------------ | ----------------- |
| **rect**     | the rect to query |

## Return Value

Returns the index of the display entirely containing the rect or closest to
the center of the rect on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.24.0.

## See Also

- [SDL_GetDisplayBounds](SDL_GetDisplayBounds)
- [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

