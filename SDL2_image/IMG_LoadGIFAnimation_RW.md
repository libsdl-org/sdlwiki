###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadGIFAnimation_RW

Load a GIF animation directly.

## Header File

Defined in [<SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/SDL2/include/SDL_image.h)

## Syntax

```c
IMG_Animation * IMG_LoadGIFAnimation_RW(SDL_RWops *src);
```

## Function Parameters

|             |         |                                           |
| ----------- | ------- | ----------------------------------------- |
| SDL_RWops * | **src** | an SDL_RWops that data will be read from. |

## Return Value

([IMG_Animation](IMG_Animation) *) Returns a new
[IMG_Animation](IMG_Animation), or NULL on error.

## Remarks

If you know you definitely have a GIF image, you can call this function,
which will skip SDL_image's file format detection routines. Generally it's
better to use the abstract interfaces; also, there is only an SDL_RWops
interface available here.

## Version

This function is available since SDL_image 2.6.0.

## See Also

- [IMG_LoadAnimation](IMG_LoadAnimation)
- [IMG_LoadAnimation_RW](IMG_LoadAnimation_RW)
- [IMG_LoadAnimationTyped_RW](IMG_LoadAnimationTyped_RW)
- [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

