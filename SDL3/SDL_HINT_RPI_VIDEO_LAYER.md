# SDL_HINT_RPI_VIDEO_LAYER

A variable controlling which Dispmanx layer to use on a Raspberry PI.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RPI_VIDEO_LAYER "SDL_RPI_VIDEO_LAYER"
```

## Remarks

Also known as Z-order. The variable can take a negative or positive value.
The default is 10000.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

