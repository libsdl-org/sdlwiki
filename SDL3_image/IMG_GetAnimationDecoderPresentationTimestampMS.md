###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_GetAnimationDecoderPresentationTimestampMS

Get the presentation timestamp of a frame in milliseconds.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
int IMG_GetAnimationDecoderPresentationTimestampMS(IMG_AnimationDecoder *decoder, Sint64 pts);
```

## Function Parameters

|                                                |             |                                        |
| ---------------------------------------------- | ----------- | -------------------------------------- |
| [IMG_AnimationDecoder](IMG_AnimationDecoder) * | **decoder** | the animation decoder.                 |
| Sint64                                         | **pts**     | the presentation timestamp to convert. |

## Return Value

(int) Returns the presentation timestamp in milliseconds.

## Remarks

This function converts a presentation timestamp from the decoder's timebase
to milliseconds.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_GetNextAnimationDecoderFrame](IMG_GetNextAnimationDecoderFrame)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

