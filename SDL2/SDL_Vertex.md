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





----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryRender](CategoryRender)

