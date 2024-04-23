###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Rect

A rectangle, with the origin at the upper left (integer).

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
typedef struct SDL_Rect
{
    int x, y;
    int w, h;
} SDL_Rect;
```

## Code Examples

```c
SDL_Rect srcrect;
SDL_Rect dstrect;

srcrect.x = 0;
srcrect.y = 0;
srcrect.w = 32;
srcrect.h = 32;
dstrect.x = 640/2;
dstrect.y = 480/2;
dstrect.w = 0;
dstrect.h = 0;

extern SDL_Surface *src, *dst;
SDL_BlitSurface(src, &srcrect, dst, &dstrect);
```

## See Also

* [SDL_RectEmpty](SDL_RectEmpty)
* [SDL_RectEquals](SDL_RectEquals)
* [SDL_HasIntersection](SDL_HasIntersection)
* [SDL_IntersectRect](SDL_IntersectRect)
* [SDL_IntersectRectAndLine](SDL_IntersectRectAndLine)
* [SDL_UnionRect](SDL_UnionRect)
* [SDL_EnclosePoints](SDL_EnclosePoints)


## Data Fields

{|
|int
|'''x'''
|the x location of the rectangle's upper left corner
|-
|int
|'''y'''
|the y location of the rectangle's upper left corner
|-
|int
|'''w'''
|the width of the rectangle
|-
|int
|'''h'''
|the height of the rectangle
|}

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryRect](CategoryRect)


