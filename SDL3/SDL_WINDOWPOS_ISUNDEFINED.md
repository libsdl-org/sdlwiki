# SDL_WINDOWPOS_ISUNDEFINED

A macro to test if the window position is marked as "undefined."

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
#define SDL_WINDOWPOS_ISUNDEFINED(X)    (((X)&0xFFFF0000) == SDL_WINDOWPOS_UNDEFINED_MASK)
```

## Macro Parameters

|       |                            |
| ----- | -------------------------- |
| **X** | the window position value. |

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_SetWindowPosition](SDL_SetWindowPosition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVideo](CategoryVideo)

