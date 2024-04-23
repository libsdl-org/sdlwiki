###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RendererInfo

Information on the capabilities of a render driver or context.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
typedef struct SDL_RendererInfo
{
    const char *name;           /**< The name of the renderer */
    Uint32 flags;               /**< Supported ::SDL_RendererFlags */
    Uint32 num_texture_formats; /**< The number of available texture formats */
    Uint32 texture_formats[16]; /**< The available texture formats */
    int max_texture_width;      /**< The maximum texture width */
    int max_texture_height;     /**< The maximum texture height */
} SDL_RendererInfo;
```

## Data Fields

|             |                           |                                                             |
| ----------- | ------------------------- | ----------------------------------------------------------- |
| const char* | '''name'''                | the name of the renderer                                    |
| Uint32      | '''flags'''               | a mask of supported renderer flags; see Remarks for details |
| Uint32      | '''num_texture_formats''' | the number of available texture formats                     |
| Uint32[16]  | '''texture_formats'''     | the available texture formats; see Remarks for details      |
| int         | '''max_texture_width'''   | the maximum texture width                                   |
| int         | '''max_texture_height'''  | the maximum texture height                                  |

## Related Enumerations

[SDL_BlendMode](SDL_BlendMode)
[SDL_PixelFormatEnum](SDL_PixelFormatEnum)
[SDL_RendererFlags](SDL_RendererFlags)
[SDL_TextureModulate](SDL_TextureModulate)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryRender](CategoryRender)


