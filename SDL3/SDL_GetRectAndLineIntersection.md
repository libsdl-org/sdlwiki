###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRectAndLineIntersection

Calculate the intersection of a rectangle and line segment.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_bool SDL_GetRectAndLineIntersection(const SDL_Rect *
                                  rect, int *X1,
                                  int *Y1, int *X2,
                                  int *Y2);

```

## Function Parameters

|              |                                                                           |
| ------------ | ------------------------------------------------------------------------- |
| **rect**     | an [SDL_Rect](SDL_Rect) structure representing the rectangle to intersect |
| **X1**       | a pointer to the starting X-coordinate of the line                        |
| **Y1**       | a pointer to the starting Y-coordinate of the line                        |
| **X2**       | a pointer to the ending X-coordinate of the line                          |
| **Y2**       | a pointer to the ending Y-coordinate of the line                          |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if there is an intersection,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This function is used to clip a line segment to a rectangle. A line segment
contained entirely within the rectangle or that does not intersect will
remain unchanged. A line segment that crosses the rectangle at either or
both ends will be clipped to the boundary of the rectangle and the new
coordinates saved in `X1`, `Y1`, `X2`, and/or `Y2` as necessary.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

