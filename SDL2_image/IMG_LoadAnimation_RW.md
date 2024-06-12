###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadAnimation_RW

Load an animation from an SDL_RWops.

## Header File

Defined in [<SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/SDL2/include/SDL_image.h)

## Syntax

```c
IMG_Animation * IMG_LoadAnimation_RW(SDL_RWops *src, int freesrc);
```

## Function Parameters

|             |             |                                                                               |
| ----------- | ----------- | ----------------------------------------------------------------------------- |
| SDL_RWops * | **src**     | an SDL_RWops that data will be read from.                                     |
| int         | **freesrc** | non-zero to close/free the SDL_RWops before returning, zero to leave it open. |

## Return Value

([IMG_Animation](IMG_Animation) *) Returns a new
[IMG_Animation](IMG_Animation), or NULL on error.

## Remarks

If `freesrc` is non-zero, the RWops will be closed before returning,
whether this function succeeds or not. SDL_image reads everything it needs
from the RWops during this call in any case.

When done with the returned animation, the app should dispose of it with a
call to [IMG_FreeAnimation](IMG_FreeAnimation)().

## Version

This function is available since SDL_image 2.6.0.

## See Also

- [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

