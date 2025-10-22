###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveAnimationTyped_IO

Save an animation to an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_SaveAnimationTyped_IO(IMG_Animation *anim, SDL_IOStream *dst, bool closeio, const char *type);
```

## Function Parameters

|                                  |             |                                                                               |
| -------------------------------- | ----------- | ----------------------------------------------------------------------------- |
| [IMG_Animation](IMG_Animation) * | **anim**    | the animation to save.                                                        |
| SDL_IOStream *                   | **dst**     | an SDL_IOStream that data will be written to.                                 |
| bool                             | **closeio** | true to close/free the SDL_IOStream before returning, false to leave it open. |
| const char *                     | **type**    | a filename extension that represent this data ("GIF", etc).                   |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If you just want to save to a filename, you can use
[IMG_SaveAnimation](IMG_SaveAnimation)() instead.

If `closeio` is true, `dst` will be closed before returning, whether this
function succeeds or not.

For formats that accept a quality, a default quality of 90 will be used.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_SaveAnimation](IMG_SaveAnimation)
- [IMG_SaveANIAnimation_IO](IMG_SaveANIAnimation_IO)
- [IMG_SaveAPNGAnimation_IO](IMG_SaveAPNGAnimation_IO)
- [IMG_SaveAVIFAnimation_IO](IMG_SaveAVIFAnimation_IO)
- [IMG_SaveGIFAnimation_IO](IMG_SaveGIFAnimation_IO)
- [IMG_SaveWEBPAnimation_IO](IMG_SaveWEBPAnimation_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

