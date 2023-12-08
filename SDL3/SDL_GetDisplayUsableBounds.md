###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetDisplayUsableBounds

Get the usable desktop area represented by a display, in screen coordinates.

## Syntax

```c
int SDL_GetDisplayUsableBounds(SDL_DisplayID displayID, SDL_Rect *rect);

```

## Function Parameters

|                   |                                                                      |
| ----------------- | -------------------------------------------------------------------- |
| **displayID**     | the instance ID of the display to query                              |
| **rect**          | the [SDL_Rect](SDL_Rect.md) structure filled in with the display bounds |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This is the same area as [SDL_GetDisplayBounds](SDL_GetDisplayBounds.md)()
reports, but with portions reserved by the system removed. For example, on
Apple's macOS, this subtracts the area occupied by the menu bar and dock.

Setting a window to be fullscreen generally bypasses these unusable areas,
so these are good guidelines for the maximum space available to a
non-fullscreen window.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetDisplayBounds](SDL_GetDisplayBounds.md)
* [SDL_GetDisplays](SDL_GetDisplays.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
