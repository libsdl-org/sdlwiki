# SDL_BUTTON

Used as a mask when testing buttons in buttonstate.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)

## Syntax

```c
#define SDL_BUTTON(X)       (1 << ((X)-1))
```

## Remarks

- Button 1: Left mouse button
- Button 2: Middle mouse button
- Button 3: Right mouse button

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMouse](CategoryMouse)

