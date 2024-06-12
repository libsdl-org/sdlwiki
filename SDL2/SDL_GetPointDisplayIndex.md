###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetPointDisplayIndex

Get the index of the display containing a point

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GetPointDisplayIndex(const SDL_Point * point);
```

## Function Parameters

|                                |           |                    |
| ------------------------------ | --------- | ------------------ |
| const [SDL_Point](SDL_Point) * | **point** | the point to query |

## Return Value

(int) Returns the index of the display containing the point or a negative
error code on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 2.24.0.

## See Also

- [SDL_GetDisplayBounds](SDL_GetDisplayBounds)
- [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

