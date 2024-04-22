###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_ALLOW_ALT_TAB_WHILE_GRABBED

Specify the behavior of Alt+Tab while the keyboard is grabbed.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ALLOW_ALT_TAB_WHILE_GRABBED "SDL_ALLOW_ALT_TAB_WHILE_GRABBED"
```

## Remarks

By default, SDL emulates Alt+Tab functionality while the keyboard is
grabbed and your window is full-screen. This prevents the user from getting
stuck in your application if you've enabled keyboard grab.

The variable can be set to the following values:

- "0": SDL will not handle Alt+Tab. Your application is responsible for
  handling Alt+Tab while the keyboard is grabbed.
- "1": SDL will minimize your window when Alt+Tab is pressed (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

