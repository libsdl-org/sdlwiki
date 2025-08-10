# SDL_FRect

A rectangle stored using floating point values.

## Header File

Defined in [<SDL3/SDL_rect.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h)

## Syntax

```c
typedef struct SDL_FRect
{
    float x;
    float y;
    float w;
    float h;
} SDL_FRect;
```

## Remarks

The origin of the coordinate space is in the top-left, with increasing
values moving down and right. The properties `x` and `y` represent the
coordinates of the top-left corner of the rectangle.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_RectEmptyFloat](SDL_RectEmptyFloat)
- [SDL_RectsEqualFloat](SDL_RectsEqualFloat)
- [SDL_RectsEqualEpsilon](SDL_RectsEqualEpsilon)
- [SDL_HasRectIntersectionFloat](SDL_HasRectIntersectionFloat)
- [SDL_GetRectIntersectionFloat](SDL_GetRectIntersectionFloat)
- [SDL_GetRectAndLineIntersectionFloat](SDL_GetRectAndLineIntersectionFloat)
- [SDL_GetRectUnionFloat](SDL_GetRectUnionFloat)
- [SDL_GetRectEnclosingPointsFloat](SDL_GetRectEnclosingPointsFloat)
- [SDL_PointInRectFloat](SDL_PointInRectFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryRect](CategoryRect)

