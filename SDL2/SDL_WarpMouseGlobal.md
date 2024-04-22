###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WarpMouseGlobal

Move the mouse to the given position in global screen space.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)

## Syntax

```c
int SDL_WarpMouseGlobal(int x, int y);

```

## Function Parameters

|           |                  |
| --------- | ---------------- |
| **x**     | the x coordinate |
| **y**     | the y coordinate |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function generates a mouse motion event.

A failure of this function usually means that it is unsupported by a
platform.

Note that this function will appear to succeed, but not actually move the
mouse when used over Microsoft Remote Desktop.

## Version

This function is available since SDL 2.0.4.

## See Also

* [SDL_WarpMouseInWindow](SDL_WarpMouseInWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

