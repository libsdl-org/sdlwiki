###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadGIFAnimation_IO

Load a GIF animation directly.

## Syntax

```c
IMG_Animation * IMG_LoadGIFAnimation_IO(SDL_IOStream *src);

```

## Function Parameters

|             |                                              |
| ----------- | -------------------------------------------- |
| **src**     | an SDL_IOStream that data will be read from. |

## Return Value

Returns a new [IMG_Animation](IMG_Animation), or NULL on error.

## Remarks

If you know you definitely have a GIF image, you can call this function,
which will skip SDL_image's file format detection routines. Generally it's
better to use the abstract interfaces; also, there is only an SDL_IOStream
interface available here.

## Version

This function is available since SDL_image 3.0.0.

## Related Functions

* [IMG_LoadAnimation](IMG_LoadAnimation)
* [IMG_LoadAnimation_IO](IMG_LoadAnimation_IO)
* [IMG_LoadAnimationTyped_IO](IMG_LoadAnimationTyped_IO)
* [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI)

