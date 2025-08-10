###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CloseAnimationDecoder

Close an animation decoder, finishing any decoding.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_CloseAnimationDecoder(IMG_AnimationDecoder *decoder);
```

## Function Parameters

|                                                |             |                       |
| ---------------------------------------------- | ----------- | --------------------- |
| [IMG_AnimationDecoder](IMG_AnimationDecoder) * | **decoder** | the decoder to close. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Calling this function frees the animation decoder, and returns the final
status of the decoding process.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationDecoder](IMG_CreateAnimationDecoder)
- [IMG_CreateAnimationDecoder_IO](IMG_CreateAnimationDecoder_IO)
- [IMG_CreateAnimationDecoderWithProperties](IMG_CreateAnimationDecoderWithProperties)
- [IMG_CreateAnimationDecoderWithProperties](IMG_CreateAnimationDecoderWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

