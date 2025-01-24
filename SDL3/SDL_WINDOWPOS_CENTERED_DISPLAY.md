# SDL_WINDOWPOS_CENTERED_DISPLAY

Used to indicate that the window position should be centered.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
#define SDL_WINDOWPOS_CENTERED_DISPLAY(X)  (SDL_WINDOWPOS_CENTERED_MASK|(X))
```

## Macro Parameters

|       |                                                           |
| ----- | --------------------------------------------------------- |
| **X** | the [SDL_DisplayID](SDL_DisplayID) of the display to use. |

## Remarks

[SDL_WINDOWPOS_CENTERED](SDL_WINDOWPOS_CENTERED) is the same, but always
uses the primary display instead of specifying one.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVideo](CategoryVideo)

