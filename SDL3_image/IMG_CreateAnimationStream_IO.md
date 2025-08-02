###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CreateAnimationStream_IO

Create an animation stream and save it to an IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_AnimationStream * IMG_CreateAnimationStream_IO(SDL_IOStream *dst, bool closeio, const char *type);
```

## Function Parameters

|                |             |                                                                   |
| -------------- | ----------- | ----------------------------------------------------------------- |
| SDL_IOStream * | **dst**     | an SDL_IOStream that will be used to save the stream.             |
| bool           | **closeio** | true to close the SDL_IOStream when done, false to leave it open. |
| const char *   | **type**    | a filename extension that represent this data ("WEBP", etc).      |

## Return Value

([IMG_AnimationStream](IMG_AnimationStream) *) Returns a new
[IMG_AnimationStream](IMG_AnimationStream), or NULL on failure; call
SDL_GetError() for more information.

## Remarks

If `closeio` is true, `dst` will be closed before returning if this
function fails, or when the animation stream is closed if this function
succeeds.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationStream](IMG_CreateAnimationStream)
- [IMG_CreateAnimationStreamWithProperties](IMG_CreateAnimationStreamWithProperties)
- [IMG_AddAnimationFrame](IMG_AddAnimationFrame)
- [IMG_CloseAnimationStream](IMG_CloseAnimationStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

