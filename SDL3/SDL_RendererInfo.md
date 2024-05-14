###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RendererInfo

Information on the capabilities of a render driver or context.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
typedef struct SDL_RendererInfo
{
    const char *name;           /**< The name of the renderer */
    int num_texture_formats;    /**< The number of available texture formats */
    const SDL_PixelFormatEnum *texture_formats; /**< The available texture formats */
} SDL_RendererInfo;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryRender](CategoryRender)

