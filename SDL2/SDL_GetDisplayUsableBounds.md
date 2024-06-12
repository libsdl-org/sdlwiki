###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDisplayUsableBounds

Get the usable desktop area represented by a display.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GetDisplayUsableBounds(int displayIndex, SDL_Rect * rect);
```

## Function Parameters

|                        |                  |                                                                      |
| ---------------------- | ---------------- | -------------------------------------------------------------------- |
| int                    | **displayIndex** | the index of the display to query the usable bounds from             |
| [SDL_Rect](SDL_Rect) * | **rect**         | the [SDL_Rect](SDL_Rect) structure filled in with the display bounds |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The primary display (`displayIndex` zero) is always located at 0,0.

This is the same area as [SDL_GetDisplayBounds](SDL_GetDisplayBounds)()
reports, but with portions reserved by the system removed. For example, on
Apple's macOS, this subtracts the area occupied by the menu bar and dock.

Setting a window to be fullscreen generally bypasses these unusable areas,
so these are good guidelines for the maximum space available to a
non-fullscreen window.

The parameter `rect` is ignored if it is NULL.

This function also returns -1 if the parameter `displayIndex` is out of
range.

## Version

This function is available since SDL 2.0.5.

## See Also

- [SDL_GetDisplayBounds](SDL_GetDisplayBounds)
- [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

