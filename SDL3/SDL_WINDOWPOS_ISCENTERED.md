# SDL_WINDOWPOS_ISCENTERED

A macro to test if the window position is marked as "centered."

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
#define SDL_WINDOWPOS_ISCENTERED(X)    \
            (((X)&0xFFFF0000) == SDL_WINDOWPOS_CENTERED_MASK)
```

## Macro Parameters

|       |                            |
| ----- | -------------------------- |
| **X** | the window position value. |

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVideo](CategoryVideo)

