# SDL_GetMouseFocus

Get the window which currently has mouse focus.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_Window * SDL_GetMouseFocus(void);
```

## Return Value

([SDL_Window](SDL_Window) *) Returns the window with mouse focus.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

