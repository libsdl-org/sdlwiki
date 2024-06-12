###### (This function is part of SDL_image, a separate library from SDL.)
# IMG_Animation

Animated image support Currently only animated GIFs are supported.

## Header File

Defined in [<SDL3_image/SDL_image.h>](https://github.com/libsdl-org/SDL_image/blob/main/include/SDL3_image/SDL_image.h)

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

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

