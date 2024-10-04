###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RectEmpty

Determine whether a rectangle has no area.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE bool SDL_RectEmpty(const SDL_Rect *r);
```

## Function Parameters

|                              |       |                        |
| ---------------------------- | ----- | ---------------------- |
| const [SDL_Rect](SDL_Rect) * | **r** | the rectangle to test. |

## Return Value

(bool) Returns true if the rectangle is "empty", false otherwise.

## Remarks

A rectangle is considered "empty" for this function if `r` is NULL, or if
`r`'s width and/or height are <= 0.

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

