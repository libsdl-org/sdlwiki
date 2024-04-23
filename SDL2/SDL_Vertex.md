###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Vertex

Vertex structure

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
typedef struct SDL_Vertex
{
    SDL_FPoint position;        /**< Vertex position, in SDL_Renderer coordinates  */
    SDL_Color  color;           /**< Vertex color */
    SDL_FPoint tex_coord;       /**< Normalized texture coordinates, if needed */
} SDL_Vertex;
```

## Data Fields

{|
|SDL_FPoint
|'''position'''
|Vertex position, in SDL_Renderer coordinates
|-
|SDL_Color
|'''color'''
|Vertex color
|-
|SDL_FPoint
|'''tex_coord'''
|Normalized texture coordinates, if needed (Range from 0 to 1, i.ie for a 64x64px texture, beginning at 32x32px will be entered as 0.5,0,5)
|}

## Related Structures

[SDL_FPoint](SDL_FPoint)
[SDL_Color](SDL_Color)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct)


