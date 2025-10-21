###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CreateAnimationDecoder_IO

Create a decoder to read a series of images from an IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_AnimationDecoder * IMG_CreateAnimationDecoder_IO(SDL_IOStream *src, bool closeio, const char *type);
```

## Function Parameters

|                |             |                                                                   |
| -------------- | ----------- | ----------------------------------------------------------------- |
| SDL_IOStream * | **src**     | an SDL_IOStream containing a series of images.                    |
| bool           | **closeio** | true to close the SDL_IOStream when done, false to leave it open. |
| const char *   | **type**    | a filename extension that represent this data ("WEBP", etc).      |

## Return Value

([IMG_AnimationDecoder](IMG_AnimationDecoder) *) Returns a new
[IMG_AnimationDecoder](IMG_AnimationDecoder), or NULL on failure; call
SDL_GetError() for more information.

## Remarks

These animation types are currently supported:

- ANI
- APNG
- AVIFS
- GIF
- WEBP

If `closeio` is true, `src` will be closed before returning if this
function fails, or when the animation decoder is closed if this function
succeeds.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationDecoder](IMG_CreateAnimationDecoder)
- [IMG_CreateAnimationDecoderWithProperties](IMG_CreateAnimationDecoderWithProperties)
- [IMG_GetAnimationDecoderFrame](IMG_GetAnimationDecoderFrame)
- [IMG_ResetAnimationDecoder](IMG_ResetAnimationDecoder)
- [IMG_CloseAnimationDecoder](IMG_CloseAnimationDecoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

