###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadAPNGAnimation_IO

Load an APNG animation directly from an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_Animation* IMG_LoadAPNGAnimation_IO(SDL_IOStream *src);
```

## Function Parameters

|                |         |                                               |
| -------------- | ------- | --------------------------------------------- |
| SDL_IOStream * | **src** | an SDL_IOStream from which data will be read. |

## Return Value

([IMG_Animation](IMG_Animation) *) Returns a new
[IMG_Animation](IMG_Animation), or NULL on error.

## Remarks

If you know you definitely have an APNG image, you can call this function,
which will skip SDL_image's file format detection routines. Generally, it's
better to use the abstract interfaces; also, there is only an SDL_IOStream
interface available here.

When done with the returned animation, the app should dispose of it with a
call to [IMG_FreeAnimation](IMG_FreeAnimation)().

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_LoadAnimation](IMG_LoadAnimation)
- [IMG_LoadAnimation_IO](IMG_LoadAnimation_IO)
- [IMG_LoadAnimationTyped_IO](IMG_LoadAnimationTyped_IO)
- [IMG_LoadAVIFAnimation_IO](IMG_LoadAVIFAnimation_IO)
- [IMG_LoadGIFAnimation_IO](IMG_LoadGIFAnimation_IO)
- [IMG_LoadWEBPAnimation_IO](IMG_LoadWEBPAnimation_IO)
- [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

