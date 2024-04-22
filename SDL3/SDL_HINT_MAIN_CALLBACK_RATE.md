###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MAIN_CALLBACK_RATE

Request [SDL_AppIterate](SDL_AppIterate)() be called at a specific rate.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MAIN_CALLBACK_RATE "SDL_MAIN_CALLBACK_RATE"
```

## Remarks

This number is in Hz, so "60" means try to iterate 60 times per second.

On some platforms, or if you are using [SDL_main](SDL_main) instead of
[SDL_AppIterate](SDL_AppIterate), this hint is ignored. When the hint can
be used, it is allowed to be changed at any time.

This defaults to 60, and specifying NULL for the hint's value will restore
the default.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

