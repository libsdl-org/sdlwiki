###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlendOperation

The blend operation used when combining source and destination pixel components.

## Header File

Defined in [<SDL3/SDL_blendmode.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_blendmode.h)

## Syntax

```c
typedef enum SDL_BlendOperation
{
    SDL_BLENDOPERATION_ADD              = 0x1,  /**< dst + src: supported by all renderers */
    SDL_BLENDOPERATION_SUBTRACT         = 0x2,  /**< src - dst : supported by D3D9, D3D11, OpenGL, OpenGLES */
    SDL_BLENDOPERATION_REV_SUBTRACT     = 0x3,  /**< dst - src : supported by D3D9, D3D11, OpenGL, OpenGLES */
    SDL_BLENDOPERATION_MINIMUM          = 0x4,  /**< min(dst, src) : supported by D3D9, D3D11 */
    SDL_BLENDOPERATION_MAXIMUM          = 0x5   /**< max(dst, src) : supported by D3D9, D3D11 */
} SDL_BlendOperation;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryBlendmode](CategoryBlendmode)

