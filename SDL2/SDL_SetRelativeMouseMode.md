###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetRelativeMouseMode

Set relative mouse mode.

## Syntax

```c
int SDL_SetRelativeMouseMode(SDL_bool enabled);

```

## Function Parameters

|                 |                                                                                  |
| --------------- | -------------------------------------------------------------------------------- |
| **enabled**     | [SDL_TRUE](SDL_TRUE) to enable relative mode, [SDL_FALSE](SDL_FALSE) to disable. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

If relative mode is not supported, this returns -1.

## Remarks

While the mouse is in relative mode, the cursor is hidden, and the driver
will try to report continuous motion in the current window. Only relative
motion events will be delivered, the mouse position will not change.

Note that this function will not be able to provide continuous relative
motion when used over Microsoft Remote Desktop, instead motion is limited
to the bounds of the screen.

This function will flush any pending mouse motion.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetRelativeMouseMode](SDL_GetRelativeMouseMode)

----
[CategoryAPI](CategoryAPI)

