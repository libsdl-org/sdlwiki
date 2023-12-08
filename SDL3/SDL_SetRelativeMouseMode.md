###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_SetRelativeMouseMode

Set relative mouse mode.

## Syntax

```c
int SDL_SetRelativeMouseMode(SDL_bool enabled);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **enabled**     | [SDL_TRUE](SDL_TRUE.md) to enable relative mode, [SDL_FALSE](SDL_FALSE.md) to disable. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

While the mouse is in relative mode, the cursor is hidden, the mouse
position is constrained to the window, and SDL will report continuous
relative mouse motion even if the mouse is at the edge of the window.

This function will flush any pending mouse motion.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRelativeMouseMode](SDL_GetRelativeMouseMode.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMouse](CategoryMouse.md), [CategoryDraft](CategoryDraft.md)
