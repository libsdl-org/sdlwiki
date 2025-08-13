###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_GetAnimationDecoderFrame

Get the next frame in an animation decoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_GetAnimationDecoderFrame(IMG_AnimationDecoder *decoder, SDL_Surface **frame, Uint64 *duration);
```

## Function Parameters

|                                                |              |                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [IMG_AnimationDecoder](IMG_AnimationDecoder) * | **decoder**  | the animation decoder.                                                                                                                                                                                                                                       |
| SDL_Surface **                                 | **frame**    | a pointer filled in with the SDL_Surface for the next frame in the animation.                                                                                                                                                                                |
| Uint64 *                                       | **duration** | the duration of the frame, usually in milliseconds but can be other units if the [`IMG_PROP_ANIMATION_DECODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER`](IMG_PROP_ANIMATION_DECODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER) property is set when creating the decoder. |

## Return Value

(bool) Returns true on success or false on failure and when no more frames
are available; call SDL_GetError() for more information.

## Remarks

This function decodes the next frame in the animation decoder, returning it
as an SDL_Surface. The returned surface should be freed with
SDL_FreeSurface() when no longer needed.

If the animation decoder has no more frames or an error occurred while
decoding the frame, this function returns false. In that case, please call
SDL_GetError() for more information. If SDL_GetError() returns an empty
string, that means there are no more available frames. If SDL_GetError()
returns a valid string, that means the decoding failed.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationDecoder](IMG_CreateAnimationDecoder)
- [IMG_CreateAnimationDecoder_IO](IMG_CreateAnimationDecoder_IO)
- [IMG_CreateAnimationDecoderWithProperties](IMG_CreateAnimationDecoderWithProperties)
- [IMG_ResetAnimationDecoder](IMG_ResetAnimationDecoder)
- [IMG_CloseAnimationDecoder](IMG_CloseAnimationDecoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

