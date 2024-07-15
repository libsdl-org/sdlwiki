###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlendMode

A set of blend modes used in drawing operations.

## Header File

Defined in [<SDL3/SDL_blendmode.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_blendmode.h)

## Syntax

```c
typedef Uint32 SDL_BlendMode;

#define SDL_BLENDMODE_NONE                  0x00000000u /**< no blending: dstRGBA = srcRGBA */
#define SDL_BLENDMODE_BLEND                 0x00000001u /**< alpha blending: dstRGB = (srcRGB * srcA) + (dstRGB * (1-srcA)), dstA = srcA + (dstA * (1-srcA)) */
#define SDL_BLENDMODE_BLEND_PREMULTIPLIED   0x00000010u /**< pre-multiplied alpha blending: dstRGBA = srcRGBA + (dstRGBA * (1-srcA)) */
#define SDL_BLENDMODE_ADD                   0x00000002u /**< additive blending: dstRGB = (srcRGB * srcA) + dstRGB, dstA = dstA */
#define SDL_BLENDMODE_ADD_PREMULTIPLIED     0x00000020u /**< pre-multiplied additive blending: dstRGB = srcRGB + dstRGB, dstA = dstA */
#define SDL_BLENDMODE_MOD                   0x00000004u /**< color modulate: dstRGB = srcRGB * dstRGB, dstA = dstA */
#define SDL_BLENDMODE_MUL                   0x00000008u /**< color multiply: dstRGB = (srcRGB * dstRGB) + (dstRGB * (1-srcA)), dstA = dstA */
#define SDL_BLENDMODE_INVALID   0x7FFFFFFFu
```

## Remarks

These predefined blend modes are supported everywhere.

Additional values may be obtained from
[SDL_ComposeCustomBlendMode](SDL_ComposeCustomBlendMode).

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_ComposeCustomBlendMode](SDL_ComposeCustomBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryBlendmode](CategoryBlendmode)

