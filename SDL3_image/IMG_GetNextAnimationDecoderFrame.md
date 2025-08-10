###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_GetNextAnimationDecoderFrame

Get the next frame in an animation decoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_GetNextAnimationDecoderFrame(IMG_AnimationDecoder *decoder, SDL_Surface** frame, Sint64* pts);
```

## Function Parameters

|                                                |             |                                                                                                              |
| ---------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------ |
| [IMG_AnimationDecoder](IMG_AnimationDecoder) * | **decoder** | the animation decoder.                                                                                       |
| Sint64 *                                       | **pts**     | a pointer to a Sint64 variable that will be set to the presentation timestamp of the frame, in milliseconds. |

## Return Value

(bool) Returns a new SDL_Surface containing the decoded frame, or NULL on
error; call SDL_GetError() for more information.

## Remarks

This function decodes the next frame in the animation decoder, returning it
as an SDL_Surface. The returned surface should be freed with
SDL_FreeSurface() when no longer needed.

If the animation decoder has no more frames, this function returns NULL and
only sets the error if the decoding has failed.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [SDL_FreeSurface](SDL_FreeSurface)
- [IMG_GetAnimationDecoderPresentationTimestampMS](IMG_GetAnimationDecoderPresentationTimestampMS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

