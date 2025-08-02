###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_CreateAnimationStream

Create an animation stream and save it to a file.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_AnimationStream * IMG_CreateAnimationStream(const char *file);
```

## Function Parameters

|              |          |                                             |
| ------------ | -------- | ------------------------------------------- |
| const char * | **file** | the file where the animation will be saved. |

## Return Value

([IMG_AnimationStream](IMG_AnimationStream) *) Returns a new
[IMG_AnimationStream](IMG_AnimationStream), or NULL on failure; call
SDL_GetError() for more information.

## Remarks

The file type is determined from the file extension, e.g. "file.webp" will
be encoded using WEBP.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_CreateAnimationStream_IO](IMG_CreateAnimationStream_IO)
- [IMG_CreateAnimationStreamWithProperties](IMG_CreateAnimationStreamWithProperties)
- [IMG_AddAnimationFrame](IMG_AddAnimationFrame)
- [IMG_CloseAnimationStream](IMG_CloseAnimationStream)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

