###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_Animation

A struct representing a series of frames (SDL_Surface) in an animation.

## Syntax

```c
IMG_Animation * animation = IMG_LoadAnimation("my_gif.gif");

```

## Function Parameters

|             |                                           |
| ----------- | ----------------------------------------- |
| **w**       | An integer that represents the width, in pixels, of the animation. |
| **h**       | An integer that represents the height, in pixels, of the animation.|
| **count**   | An integer that represents the number of frames in the animation.  |
| **frames**  | A pointer to an array of SDL_Surface pointers with length of count.|
| **delays**  | A pointer to an array of integers that represent the time in milliseconds each frame should be displayed. Has length of count.|

## Remarks

Currently only animated GIFs are supported.

## Version

This struct is available since SDL_image ?.?.?.

## Related Functions

* [IMG_LoadAnimation](IMG_LoadAnimation)
* [IMG_LoadAnimation_RW](IMG_LoadAnimation_RW)
* [IMG_LoadAnimationTyped_RW](IMG_LoadAnimationTyped_RW)
* [IMG_FreeAnimation](IMG_FreeAnimation)

----
[CategoryAPI](CategoryAPI)

