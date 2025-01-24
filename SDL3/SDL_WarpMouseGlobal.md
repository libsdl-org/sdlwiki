# SDL_WarpMouseGlobal

Move the mouse to the given position in global screen space.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
bool SDL_WarpMouseGlobal(float x, float y);
```

## Function Parameters

|       |       |                   |
| ----- | ----- | ----------------- |
| float | **x** | the x coordinate. |
| float | **y** | the y coordinate. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function generates a mouse motion event.

A failure of this function usually means that it is unsupported by a
platform.

Note that this function will appear to succeed, but not actually move the
mouse when used over Microsoft Remote Desktop.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_WarpMouseInWindow](SDL_WarpMouseInWindow)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

