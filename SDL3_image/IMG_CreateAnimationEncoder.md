###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CreateAnimationEncoder

Create an encoder to save a series of images to a file.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_AnimationEncoder * IMG_CreateAnimationEncoder(const char *file);
```

## Function Parameters

|              |          |                                             |
| ------------ | -------- | ------------------------------------------- |
| const char * | **file** | the file where the animation will be saved. |

## Return Value

([IMG_AnimationEncoder](IMG_AnimationEncoder) *) Returns a new
[IMG_AnimationEncoder](IMG_AnimationEncoder), or NULL on failure; call
SDL_GetError() for more information.

## Remarks

The file type is determined from the file extension, e.g. "file.webp" will
be encoded using WEBP.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationEncoder_IO](IMG_CreateAnimationEncoder_IO)
- [IMG_CreateAnimationEncoderWithProperties](IMG_CreateAnimationEncoderWithProperties)
- [IMG_AddAnimationEncoderFrame](IMG_AddAnimationEncoderFrame)
- [IMG_CloseAnimationEncoder](IMG_CloseAnimationEncoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

