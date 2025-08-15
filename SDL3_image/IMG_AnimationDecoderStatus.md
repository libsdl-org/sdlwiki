###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_AnimationDecoderStatus

An enum representing the status of an animation decoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
typedef enum IMG_AnimationDecoderStatus
{
    IMG_DECODER_STATUS_INVALID = -1,    /**< The decoder is invalid */
    IMG_DECODER_STATUS_OK,              /**< The decoder is ready to decode the next frame */
    IMG_DECODER_STATUS_FAILED,          /**< The decoder failed to decode a frame, call SDL_GetError() for more information. */
    IMG_DECODER_STATUS_COMPLETE         /**< No more frames available */
} IMG_AnimationDecoderStatus;
```

## Version

This enum is available since SDL_image 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySDLImage](CategorySDLImage)

