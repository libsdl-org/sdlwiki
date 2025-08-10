###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_ResetAnimationDecoder

Reset the animation decoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_ResetAnimationDecoder(IMG_AnimationDecoder *decoder);
```

## Function Parameters

|                                                |             |                       |
| ---------------------------------------------- | ----------- | --------------------- |
| [IMG_AnimationDecoder](IMG_AnimationDecoder) * | **decoder** | the decoder to reset. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

Calling this function resets the animation decoder, allowing it to start
from the beginning again. This is useful if you want to decode the frame
sequence again without creating a new decoder.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_GetNextAnimationDecoderFrame](IMG_GetNextAnimationDecoderFrame)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

