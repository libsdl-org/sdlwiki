###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PointInRect

Determine whether a point resides inside a rectangle.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_PointInRect(const SDL_Point *p, const SDL_Rect *r);
```

## Function Parameters

|           |                        |
| --------- | ---------------------- |
| **p**     | the point to test.     |
| **r**     | the rectangle to test. |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if `p` is contained by `r`,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

A point is considered part of a rectangle if both `p` and `r` are not NULL,
and `p`'s x and y coordinates are >= to the rectangle's top left corner,
and < the rectangle's x+w and y+h. So a 1x1 rectangle considers point (0,0)
as "inside" and (0,1) as not.

Note that this is a forced-inline function in a header, and not a public
API function available in the SDL library (which is to say, the code is
embedded in the calling program and the linker and dynamic loader will not
be able to find this function inside SDL itself).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

