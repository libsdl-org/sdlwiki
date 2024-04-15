###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlendFactor

The normalized factor used to multiply pixel components.

## Header File

Defined in [SDL_blendmode.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_blendmode.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef enum SDL_BlendFactor
{
    SDL_BLENDFACTOR_ZERO                = 0x1,  /**< 0, 0, 0, 0 */
    SDL_BLENDFACTOR_ONE                 = 0x2,  /**< 1, 1, 1, 1 */
    SDL_BLENDFACTOR_SRC_COLOR           = 0x3,  /**< srcR, srcG, srcB, srcA */
    SDL_BLENDFACTOR_ONE_MINUS_SRC_COLOR = 0x4,  /**< 1-srcR, 1-srcG, 1-srcB, 1-srcA */
    SDL_BLENDFACTOR_SRC_ALPHA           = 0x5,  /**< srcA, srcA, srcA, srcA */
    SDL_BLENDFACTOR_ONE_MINUS_SRC_ALPHA = 0x6,  /**< 1-srcA, 1-srcA, 1-srcA, 1-srcA */
    SDL_BLENDFACTOR_DST_COLOR           = 0x7,  /**< dstR, dstG, dstB, dstA */
    SDL_BLENDFACTOR_ONE_MINUS_DST_COLOR = 0x8,  /**< 1-dstR, 1-dstG, 1-dstB, 1-dstA */
    SDL_BLENDFACTOR_DST_ALPHA           = 0x9,  /**< dstA, dstA, dstA, dstA */
    SDL_BLENDFACTOR_ONE_MINUS_DST_ALPHA = 0xA   /**< 1-dstA, 1-dstA, 1-dstA, 1-dstA */
} SDL_BlendFactor;
```

## Remarks

The blend factors are multiplied with the pixels from a drawing operation
(src) and the pixels from the render target (dst) before the blend
operation. The comma-separated factors listed above are always applied in
the component order red, green, blue, and alpha.

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

