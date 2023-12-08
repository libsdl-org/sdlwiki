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

While the mouse is in relative mode, the cursor is hidden, the mouse
position is constrained to the window, and SDL will report continuous
relative mouse motion even if the mouse is at the edge of the window.

This function will flush any pending mouse motion.

You will need to use [SDL_GetRelativeMouseState](https://wiki.libsdl.org/SDL2/SDL_GetRelativeMouseState) the retrieve the relative mouse coordinates.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetRelativeMouseMode](SDL_GetRelativeMouseMode)

----
[CategoryAPI](CategoryAPI)

