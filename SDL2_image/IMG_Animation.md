###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_Animation

Animated image support.

## Header File

Defined in [<SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/SDL2/include/SDL_image.h)

## Syntax

```c
typedef struct IMG_Animation
{
	int w, h;
	int count;
	SDL_Surface **frames;
	int *delays;
} IMG_Animation;
```

## Remarks

Currently only animated GIFs are supported.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

