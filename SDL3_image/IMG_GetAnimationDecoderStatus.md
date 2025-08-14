###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_GetAnimationDecoderStatus

Get the decoder status indicating the current state of the decoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_AnimationDecoderStatus IMG_GetAnimationDecoderStatus(IMG_AnimationDecoder *decoder);
```

## Function Parameters

|                                                |             |                                   |
| ---------------------------------------------- | ----------- | --------------------------------- |
| [IMG_AnimationDecoder](IMG_AnimationDecoder) * | **decoder** | the decoder to get the status of. |

## Return Value

([IMG_AnimationDecoderStatus](IMG_AnimationDecoderStatus)) Returns the
status of the underlying decoder, or
[IMG_DECODER_STATUS_INVALID](IMG_DECODER_STATUS_INVALID) if the given
decoder is invalid.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_GetAnimationDecoderFrame](IMG_GetAnimationDecoderFrame)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

