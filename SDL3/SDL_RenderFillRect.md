###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderFillRect

Fill a rectangle on the current rendering target with the drawing color at subpixel precision.

## Syntax

```c
int SDL_RenderFillRect(SDL_Renderer *renderer, const SDL_FRect *rect);

```

## Function Parameters

|                  |                                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| **renderer**     | The renderer which should fill a rectangle.                                      |
| **rect**         | A pointer to the destination rectangle, or NULL for the entire rendering target. |

## Return Value

Returns 0 on success, or -1 on error

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategoryRender](CategoryRender.md)
