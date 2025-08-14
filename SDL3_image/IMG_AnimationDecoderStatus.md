###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_AnimationDecoderStatus

An enum representing the status of the encoder and decoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
typedef enum IMG_AnimationDecoderStatus
{
    IMG_DECODER_STATUS_OK,          /**< Decoded the frame successfully. */
    IMG_DECODER_STATUS_FAILED,      /**< Decoding the frame failed. Call SDL_GetError for more information. */
    IMG_DECODER_STATUS_COMPLETE,    /**< No more frames available. */

    IMG_DECODER_STATUS_INVALID      /**< Invalid decoder status that does not represent any valid status. */
} IMG_AnimationDecoderStatus;
```

## Version

This enum is available since SDL_image 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySDLImage](CategorySDLImage)

