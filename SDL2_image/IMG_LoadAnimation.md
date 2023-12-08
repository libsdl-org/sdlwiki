###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_LoadAnimation

Load an animation from a file.

## Syntax

```c
IMG_Animation * IMG_LoadAnimation(const char *file);

```

## Function Parameters

|              |                                                      |
| ------------ | ---------------------------------------------------- |
| **file**     | path on the filesystem containing an animated image. |

## Return Value

Returns a new [IMG_Animation](IMG_Animation.md), or NULL on error.

## Remarks

When done with the returned animation, the app should dispose of it with a
call to [IMG_FreeAnimation](IMG_FreeAnimation.md)().

## Version

This function is available since SDL_image 2.6.0.

## Related Functions

* [IMG_FreeAnimation](IMG_FreeAnimation.md)

----
[CategoryAPI](CategoryAPI.md)
