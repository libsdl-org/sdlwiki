###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CreateAnimationEncoder_IO

Create an encoder to save a series of images to an IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_AnimationEncoder * IMG_CreateAnimationEncoder_IO(SDL_IOStream *dst, bool closeio, const char *type);
```

## Function Parameters

|                |             |                                                                   |
| -------------- | ----------- | ----------------------------------------------------------------- |
| SDL_IOStream * | **dst**     | an SDL_IOStream that will be used to save the stream.             |
| bool           | **closeio** | true to close the SDL_IOStream when done, false to leave it open. |
| const char *   | **type**    | a filename extension that represent this data ("WEBP", etc).      |

## Return Value

([IMG_AnimationEncoder](IMG_AnimationEncoder) *) Returns a new
[IMG_AnimationEncoder](IMG_AnimationEncoder), or NULL on failure; call
SDL_GetError() for more information.

## Remarks

If `closeio` is true, `dst` will be closed before returning if this
function fails, or when the animation encoder is closed if this function
succeeds.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationEncoder](IMG_CreateAnimationEncoder)
- [IMG_CreateAnimationEncoderWithProperties](IMG_CreateAnimationEncoderWithProperties)
- [IMG_AddAnimationEncoderFrame](IMG_AddAnimationEncoderFrame)
- [IMG_CloseAnimationEncoder](IMG_CloseAnimationEncoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

