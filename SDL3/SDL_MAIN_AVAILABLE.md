# SDL_MAIN_AVAILABLE

Defined if the target platform offers a special mainline through SDL.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
#define SDL_MAIN_AVAILABLE
```

## Remarks

This won't be defined otherwise. If defined, SDL's headers will redefine
`main` to [`SDL_main`](SDL_main).

This macro is defined by `SDL_main.h`, which is not automatically included
by `SDL.h`.

Even if available, an app can define [SDL_MAIN_HANDLED](SDL_MAIN_HANDLED)
and provide their own, if they know what they're doing.

This macro is used internally by SDL, and apps probably shouldn't rely on
it.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMain](CategoryMain)

