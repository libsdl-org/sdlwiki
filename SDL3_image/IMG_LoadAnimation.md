###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadAnimation

Load an animation from a file.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

## Syntax

```c
IMG_Animation * IMG_LoadAnimation(const char *file);
```

## Function Parameters

|              |          |                                                      |
| ------------ | -------- | ---------------------------------------------------- |
| const char * | **file** | path on the filesystem containing an animated image. |

## Return Value

([IMG_Animation](IMG_Animation) *) Returns a new
[IMG_Animation](IMG_Animation), or NULL on error.

## Remarks

When done with the returned animation, the app should dispose of it with a
call to [IMG_FreeAnimation](IMG_FreeAnimation)().

## Version

This function is available since SDL_image 3.0.0.

## See Also

- [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

