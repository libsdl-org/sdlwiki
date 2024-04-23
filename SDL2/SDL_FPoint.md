###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FPoint

The structure that defines a point (floating point)

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
typedef struct SDL_FPoint
{
    float x;
    float y;
} SDL_FPoint;
```

## See Also

* [SDL_EncloseFPoints](SDL_EncloseFPoints)
* [SDL_PointInFRect](SDL_PointInFRect)


## Data Fields

|       |         |                               |
| ----- | ------- | ----------------------------- |
| float | '''x''' | the x coordinate of the point |
| float | '''y''' | the y coordinate of the point |

## Related Structures

[SDL_Vertex](SDL_Vertex)
[SDL_FRect](SDL_FRect)
[SDL_Point](SDL_Point)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryRect](CategoryRect)


