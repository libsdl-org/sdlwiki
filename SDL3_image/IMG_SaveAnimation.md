###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_SaveAnimation

Save an animation to a file.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
bool IMG_SaveAnimation(IMG_Animation *anim, const char *file);
```

## Function Parameters

|                                  |          |                                                      |
| -------------------------------- | -------- | ---------------------------------------------------- |
| [IMG_Animation](IMG_Animation) * | **anim** | the animation to save.                               |
| const char *                     | **file** | path on the filesystem containing an animated image. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

For formats that accept a quality, a default quality of 90 will be used.

## Version

This function is available since SDL_image 3.4.0.

## See Also

- [IMG_SaveAnimationTyped_IO](IMG_SaveAnimationTyped_IO)
- [IMG_SaveANIAnimation_IO](IMG_SaveANIAnimation_IO)
- [IMG_SaveAPNGAnimation_IO](IMG_SaveAPNGAnimation_IO)
- [IMG_SaveAVIFAnimation_IO](IMG_SaveAVIFAnimation_IO)
- [IMG_SaveGIFAnimation_IO](IMG_SaveGIFAnimation_IO)
- [IMG_SaveWEBPAnimation_IO](IMG_SaveWEBPAnimation_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

