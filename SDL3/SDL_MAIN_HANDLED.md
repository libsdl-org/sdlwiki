# SDL_MAIN_HANDLED

Inform SDL that the app is providing an entry point instead of SDL.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
#define SDL_MAIN_HANDLED 1
```

## Remarks

SDL does not define this macro, but will check if it is defined when
including `SDL_main.h`. If defined, SDL will expect the app to provide the
proper entry point for the platform, and all the other magic details
needed, like manually calling [SDL_SetMainReady](SDL_SetMainReady).

Please see [README/main-functions](README/main-functions), (or
docs/README-main-functions.md in the source tree) for a more detailed
explanation.

## Version

This macro is used by the headers since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMain](CategoryMain)

