###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadAnimation_IO

Load an animation from an SDL_IOStream.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_Animation * IMG_LoadAnimation_IO(SDL_IOStream *src, SDL_bool closeio);
```

## Function Parameters

|                |             |                                                                                       |
| -------------- | ----------- | ------------------------------------------------------------------------------------- |
| SDL_IOStream * | **src**     | an SDL_IOStream that data will be read from.                                          |
| SDL_bool       | **closeio** | SDL_TRUE to close/free the SDL_IOStream before returning, SDL_FALSE to leave it open. |

## Return Value

([IMG_Animation](IMG_Animation) *) Returns a new
[IMG_Animation](IMG_Animation), or NULL on error.

## Remarks

If `closeio` is SDL_TRUE, `src` will be closed before returning, whether
this function succeeds or not. SDL_image reads everything it needs from
`src` during this call in any case.

When done with the returned animation, the app should dispose of it with a
call to [IMG_FreeAnimation](IMG_FreeAnimation)().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

