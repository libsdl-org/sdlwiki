###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_GetAnimationDecoderMetadata

Get the metadata of an animation decoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
SDL_PropertiesID IMG_GetAnimationDecoderMetadata(IMG_AnimationDecoder *decoder);
```

## Function Parameters

|                                                |             |                        |
| ---------------------------------------------- | ----------- | ---------------------- |
| [IMG_AnimationDecoder](IMG_AnimationDecoder) * | **decoder** | the animation decoder. |

## Return Value

(SDL_PropertiesID) Returns a SDL_PropertiesID containing the metadata, or 0
if there is no metadata available.

## Remarks

These are the supported properties: -
[`IMG_PROP_ANIMATION_DECODER_METADATA_FRAME_COUNT_NUMBER`](IMG_PROP_ANIMATION_DECODER_METADATA_FRAME_COUNT_NUMBER):
the number of frames in the animation. -
[`IMG_PROP_ANIMATION_DECODER_METADATA_LOOP_COUNT_NUMBER`](IMG_PROP_ANIMATION_DECODER_METADATA_LOOP_COUNT_NUMBER):
the amount of loops the animation will perform. A value of 0 means it will
loop forever.

This function returns the properties of the animation decoder, such as the
number of frames and loop count.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_GetNextAnimationDecoderFrame](IMG_GetNextAnimationDecoderFrame)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

