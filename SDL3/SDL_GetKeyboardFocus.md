# SDL_GetKeyboardFocus

Query the window which currently has keyboard focus.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Window * SDL_GetKeyboardFocus(void);
```

## Return Value

([SDL_Window](SDL_Window) *) Returns the window with keyboard focus.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

