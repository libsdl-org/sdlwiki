###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RenderLine

Draw a line on the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderLine(SDL_Renderer *renderer, float x1, float y1, float x2, float y2);

```

## Function Parameters

|                  |                                        |
| ---------------- | -------------------------------------- |
| **renderer**     | The renderer which should draw a line. |
| **x1**           | The x coordinate of the start point.   |
| **y1**           | The y coordinate of the start point.   |
| **x2**           | The x coordinate of the end point.     |
| **y2**           | The y coordinate of the end point.     |

## Return Value

Returns 0 on success, or -1 on error

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

