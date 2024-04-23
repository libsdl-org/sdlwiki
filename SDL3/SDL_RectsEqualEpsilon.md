###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RectsEqualEpsilon

Determine whether two floating point rectangles are equal, within some given epsilon.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE SDL_bool SDL_RectsEqualEpsilon(const SDL_FRect *a, const SDL_FRect *b, const float epsilon);
```

## Function Parameters

|           |                               |
| --------- | ----------------------------- |
| **a**     | the first rectangle to test.  |
| **b**     | the second rectangle to test. |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the rectangles are equal,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

Rectangles are considered equal if both are not NULL and each of their x,
y, width and height are within `epsilon` of each other. If you don't know
what value to use for `epsilon`, you should call the
[SDL_RectsEqualFloat](SDL_RectsEqualFloat) function instead.

Note that this is a forced-inline function in a header, and not a public
API function available in the SDL library (which is to say, the code is
embedded in the calling program and the linker and dynamic loader will not
be able to find this function inside SDL itself).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_RectsEqualFloat](SDL_RectsEqualFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

