# SDL_CursorFrameInfo

Animated cursor frame info.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
typedef struct SDL_CursorFrameInfo
{
    SDL_Surface *surface; /**< The surface data for this frame */
    Uint32 duration;      /**< The frame duration in milliseconds (a duration of 0 is infinite) */
} SDL_CursorFrameInfo;
```

## Version

This struct is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryMouse](CategoryMouse)

