###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadWEBPAnimation_RW

Load a WEBP animation directly.

## Syntax

```c
IMG_Animation * IMG_LoadWEBPAnimation_RW(SDL_RWops *src);

```

## Function Parameters

|             |                                           |
| ----------- | ----------------------------------------- |
| **src**     | an SDL_RWops that data will be read from. |

## Return Value

Returns a new [IMG_Animation](IMG_Animation), or NULL on error.

## Remarks

If you know you definitely have a WEBP image, you can call this function,
which will skip SDL_image's file format detection routines. Generally it's
better to use the abstract interfaces; also, there is only an SDL_RWops
interface available here.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_LoadAnimation](IMG_LoadAnimation)
* [IMG_LoadAnimation_RW](IMG_LoadAnimation_RW)
* [IMG_LoadAnimationTyped_RW](IMG_LoadAnimationTyped_RW)
* [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI)

