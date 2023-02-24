###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRectIntersection

Calculate the intersection of two rectangles.

## Syntax

```c
SDL_bool SDL_GetRectIntersection(const SDL_Rect * A,
                           const SDL_Rect * B,
                           SDL_Rect * result);

```

## Function Parameters

|                |                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------- |
| **A**          | an [SDL_Rect](SDL_Rect) structure representing the first rectangle                          |
| **B**          | an [SDL_Rect](SDL_Rect) structure representing the second rectangle                         |
| **result**     | an [SDL_Rect](SDL_Rect) structure filled in with the intersection of rectangles `A` and `B` |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if there is an intersection,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

If `result` is NULL then this function will return [SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasRectIntersection](SDL_HasRectIntersection)

----
[CategoryAPI](CategoryAPI)

