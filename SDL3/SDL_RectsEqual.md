###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RectsEqual

Determine whether two rectangles are equal.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
SDL_FORCE_INLINE bool SDL_RectsEqual(const SDL_Rect *a, const SDL_Rect *b);
```

## Function Parameters

|                              |       |                               |
| ---------------------------- | ----- | ----------------------------- |
| const [SDL_Rect](SDL_Rect) * | **a** | the first rectangle to test.  |
| const [SDL_Rect](SDL_Rect) * | **b** | the second rectangle to test. |

## Return Value

(bool) Returns true if the rectangles are equal, false otherwise.

## Remarks

Rectangles are considered equal if both are not NULL and each of their x,
y, width and height match.

Note that this is a forced-inline function in a header, and not a public
API function available in the SDL library (which is to say, the code is
embedded in the calling program and the linker and dynamic loader will not
be able to find this function inside SDL itself).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

