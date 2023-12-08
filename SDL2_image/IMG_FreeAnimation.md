###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_FreeAnimation

Dispose of an [IMG_Animation](IMG_Animation.md) and free its resources.

## Syntax

```c
void IMG_FreeAnimation(IMG_Animation *anim);

```

## Function Parameters

|              |                                               |
| ------------ | --------------------------------------------- |
| **anim**     | [IMG_Animation](IMG_Animation.md) to dispose of. |

## Remarks

The provided `anim` pointer is not valid once this call returns.

## Version

This function is available since SDL_image 2.6.0.

## Related Functions

* [IMG_LoadAnimation](IMG_LoadAnimation.md)
* [IMG_LoadAnimation_RW](IMG_LoadAnimation_RW.md)
* [IMG_LoadAnimationTyped_RW](IMG_LoadAnimationTyped_RW.md)

----
[CategoryAPI](CategoryAPI.md)
