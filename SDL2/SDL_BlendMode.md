# SDL_BlendMode

The blend mode used in [SDL_RenderCopy](SDL_RenderCopy)() and drawing operations.

## Header File

Defined in [SDL_blendmode.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_blendmode.h)

## Syntax

```c
typedef enum SDL_BlendMode
{
    SDL_BLENDMODE_NONE = 0x00000000,     /**< no blending
                                              dstRGBA = srcRGBA */
    SDL_BLENDMODE_BLEND = 0x00000001,    /**< alpha blending
                                              dstRGB = (srcRGB * srcA) + (dstRGB * (1-srcA))
                                              dstA = srcA + (dstA * (1-srcA)) */
    SDL_BLENDMODE_ADD = 0x00000002,      /**< additive blending
                                              dstRGB = (srcRGB * srcA) + dstRGB
                                              dstA = dstA */
    SDL_BLENDMODE_MOD = 0x00000004,      /**< color modulate
                                              dstRGB = srcRGB * dstRGB
                                              dstA = dstA */
    SDL_BLENDMODE_MUL = 0x00000008,      /**< color multiply
                                              dstRGB = (srcRGB * dstRGB) + (dstRGB * (1-srcA))
                                              dstA = dstA */
    SDL_BLENDMODE_INVALID = 0x7FFFFFFF

    /* Additional custom blend modes can be returned by SDL_ComposeCustomBlendMode() */

} SDL_BlendMode;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryBlendmode](CategoryBlendmode)

