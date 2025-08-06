###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_FreeAnimation

Dispose of an [IMG_Animation](IMG_Animation) and free its resources.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
void IMG_FreeAnimation(IMG_Animation *anim);
```

## Function Parameters

|                                  |          |                                               |
| -------------------------------- | -------- | --------------------------------------------- |
| [IMG_Animation](IMG_Animation) * | **anim** | [IMG_Animation](IMG_Animation) to dispose of. |

## Remarks

The provided `anim` pointer is not valid once this call returns.

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_LoadAnimation](IMG_LoadAnimation)
- [IMG_LoadAnimation_IO](IMG_LoadAnimation_IO)
- [IMG_LoadAnimationTyped_IO](IMG_LoadAnimationTyped_IO)
- [IMG_LoadAPNGAnimation_IO](IMG_LoadAPNGAnimation_IO)
- [IMG_LoadAVIFAnimation_IO](IMG_LoadAVIFAnimation_IO)
- [IMG_LoadGIFAnimation_IO](IMG_LoadGIFAnimation_IO)
- [IMG_LoadWEBPAnimation_IO](IMG_LoadWEBPAnimation_IO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLImage](CategorySDLImage)

