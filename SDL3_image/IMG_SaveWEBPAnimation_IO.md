###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveWEBPAnimation_IO

Save an animation in WEBP format to an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_SaveWEBPAnimation_IO(IMG_Animation *anim, SDL_IOStream *dst, bool closeio, int quality);
```

## Function Parameters

|                                  |             |                                                                                                                                                                                                                                             |
| -------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [IMG_Animation](IMG_Animation) * | **anim**    | the animation to save.                                                                                                                                                                                                                      |
| SDL_IOStream *                   | **dst**     | an SDL_IOStream from which data will be written to.                                                                                                                                                                                         |
| bool                             | **closeio** | true to close/free the SDL_IOStream before returning, false to leave it open.                                                                                                                                                               |
| int                              | **quality** | between 0 and 100. For lossy, 0 gives the smallest size and 100 the largest. For lossless, this parameter is the amount of effort put into the compression: 0 is the fastest but gives larger files compared to the slowest, but best, 100. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If `closeio` is true, `dst` will be closed before returning, whether this
function succeeds or not.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_SaveAnimation](IMG_SaveAnimation)
- [IMG_SaveAnimationTyped_IO](IMG_SaveAnimationTyped_IO)
- [IMG_SaveANIAnimation_IO](IMG_SaveANIAnimation_IO)
- [IMG_SaveAPNGAnimation_IO](IMG_SaveAPNGAnimation_IO)
- [IMG_SaveAVIFAnimation_IO](IMG_SaveAVIFAnimation_IO)
- [IMG_SaveGIFAnimation_IO](IMG_SaveGIFAnimation_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

