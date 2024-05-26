###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MouseButtonFlags

A bitmask of pressed mouse buttons, as reported by [SDL_GetMouseState](SDL_GetMouseState), etc.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
typedef Uint32 SDL_MouseButtonFlags;

#define SDL_BUTTON_LEFT     1
#define SDL_BUTTON_MIDDLE   2
#define SDL_BUTTON_RIGHT    3
#define SDL_BUTTON_X1       4
#define SDL_BUTTON_X2       5

#define SDL_BUTTON(X)       (1u << ((X)-1))
#define SDL_BUTTON_LMASK    SDL_BUTTON(SDL_BUTTON_LEFT)
#define SDL_BUTTON_MMASK    SDL_BUTTON(SDL_BUTTON_MIDDLE)
#define SDL_BUTTON_RMASK    SDL_BUTTON(SDL_BUTTON_RIGHT)
#define SDL_BUTTON_X1MASK   SDL_BUTTON(SDL_BUTTON_X1)
#define SDL_BUTTON_X2MASK   SDL_BUTTON(SDL_BUTTON_X2)
```

## Remarks

- Button 1: Left mouse button
- Button 2: Middle mouse button
- Button 3: Right mouse button
- Button 4: Side mouse button 1
- Button 5: Side mouse button 2

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_GetMouseState](SDL_GetMouseState)
- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)
- [SDL_GetRelativeMouseState](SDL_GetRelativeMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryMouse](CategoryMouse)

