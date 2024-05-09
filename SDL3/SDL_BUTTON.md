###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BUTTON

Used as a mask when testing buttons in buttonstate.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
#define SDL_BUTTON(X)       (1u << ((X)-1))
```

## Remarks

- Button 1: Left mouse button
- Button 2: Middle mouse button
- Button 3: Right mouse button
- Button 4: Side mouse button 1
- Button 5: Side mouse button 2

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

