###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FRect

A rectangle, with the origin at the upper left (floating point).

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

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

## Code Examples

```c++
SDL_FRect rect;

rect.x = 0.0;
rect.y = 0.0;
rect.w = 32.0;
rect.h = 32.0;
```

## Related Functions

* [SDL_FRectEmpty](SDL_FRectEmpty)
* [SDL_FRectEquals](SDL_FRectEquals)
* [SDL_FRectEqualsEpsilon](SDL_FRectEqualsEpsilon)
* [SDL_HasIntersectionF](SDL_HasIntersectionF)
* [SDL_IntersectFRect](SDL_IntersectFRect)
* [SDL_IntersectFRectAndLine](SDL_IntersectFRectAndLine)
* [SDL_UnionFRect](SDL_UnionFRect)
* [SDL_EncloseFPoints](SDL_EncloseFPoints)
* [SDL_PointInFRect](SDL_PointInFRect)


## Data Fields

{|
|float
|'''x'''
|the x location of the rectangle's upper left corner
|-
|float
|'''y'''
|the y location of the rectangle's upper left corner
|-
|float
|'''w'''
|the width of the rectangle
|-
|float
|'''h'''
|the height of the rectangle
|}

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryRect](CategoryRect)


