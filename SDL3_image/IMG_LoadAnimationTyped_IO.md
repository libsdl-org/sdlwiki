###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadAnimationTyped_IO

Load an animation from an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_Animation * IMG_LoadAnimationTyped_IO(SDL_IOStream *src, bool closeio, const char *type);
```

## Function Parameters

|                |             |                                                                               |
| -------------- | ----------- | ----------------------------------------------------------------------------- |
| SDL_IOStream * | **src**     | an SDL_IOStream that data will be read from.                                  |
| bool           | **closeio** | true to close/free the SDL_IOStream before returning, false to leave it open. |
| const char *   | **type**    | a filename extension that represent this data ("GIF", etc).                   |

## Return Value

([IMG_Animation](IMG_Animation) *) Returns a new
[IMG_Animation](IMG_Animation), or NULL on error.

## Remarks

Even though this function accepts a file type, SDL_image may still try
other decoders that are capable of detecting file type from the contents of
the image data, but may rely on the caller-provided type string for formats
that it cannot autodetect. If `type` is NULL, SDL_image will rely solely on
its ability to guess the format.

If `closeio` is true, `src` will be closed before returning, whether this
function succeeds or not. SDL_image reads everything it needs from `src`
during this call in any case.

When done with the returned animation, the app should dispose of it with a
call to [IMG_FreeAnimation](IMG_FreeAnimation)().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_CreateAnimatedCursor](IMG_CreateAnimatedCursor)
- [IMG_LoadAnimation](IMG_LoadAnimation)
- [IMG_LoadAnimation_IO](IMG_LoadAnimation_IO)
- [IMG_LoadANIAnimation_IO](IMG_LoadANIAnimation_IO)
- [IMG_LoadAPNGAnimation_IO](IMG_LoadAPNGAnimation_IO)
- [IMG_LoadAVIFAnimation_IO](IMG_LoadAVIFAnimation_IO)
- [IMG_LoadGIFAnimation_IO](IMG_LoadGIFAnimation_IO)
- [IMG_LoadWEBPAnimation_IO](IMG_LoadWEBPAnimation_IO)
- [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

