###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderRect

Draw a rectangle on the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderRect(SDL_Renderer *renderer, const SDL_FRect *rect);

```

## Function Parameters

|                  |                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------- |
| **renderer**     | The renderer which should draw a rectangle.                                             |
| **rect**         | A pointer to the destination rectangle, or NULL to outline the entire rendering target. |

## Return Value

Returns 0 on success, or -1 on error

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

