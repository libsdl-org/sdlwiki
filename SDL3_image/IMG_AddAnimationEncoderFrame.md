###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_AddAnimationEncoderFrame

Add a frame to an animation encoder.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_AddAnimationEncoderFrame(IMG_AnimationEncoder *encoder, SDL_Surface *surface, Uint64 pts);
```

## Function Parameters

|                                                |             |                                                                                                                                                                                                                                                                            |
| ---------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [IMG_AnimationEncoder](IMG_AnimationEncoder) * | **encoder** | the receiving images.                                                                                                                                                                                                                                                      |
| SDL_Surface *                                  | **surface** | the surface to add as the next frame in the animation.                                                                                                                                                                                                                     |
| Uint64                                         | **pts**     | the presentation timestamp of the frame, usually in milliseconds but can be other units if the [`IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER`](IMG_PROP_ANIMATION_ENCODER_CREATE_TIMEBASE_DENOMINATOR_NUMBER) property is set when creating the encoder. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationEncoder](IMG_CreateAnimationEncoder)
- [IMG_CreateAnimationEncoder_IO](IMG_CreateAnimationEncoder_IO)
- [IMG_CreateAnimationEncoderWithProperties](IMG_CreateAnimationEncoderWithProperties)
- [IMG_CloseAnimationEncoder](IMG_CloseAnimationEncoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

