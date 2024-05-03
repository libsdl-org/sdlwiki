###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MAIN_USE_CALLBACKS

Inform SDL to use the main callbacks instead of main.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
#define SDL_MAIN_USE_CALLBACKS 1
```

## Remarks

SDL does not define this macro, but will check if it is defined to any
value in [SDL_main](SDL_main).h. If defined, SDL will expect the app to
provide several functions: [SDL_AppInit](SDL_AppInit),
[SDL_AppEvent](SDL_AppEvent), [SDL_AppIterate](SDL_AppIterate), and
[SDL_AppQuit](SDL_AppQuit). The app should not provide a `main` function in
this case, and doing so will likely cause the build to fail.

Please see [README/main-functions](README/main-functions), (or
docs/README-main-functions.md in the source tree) for a more detailed
explanation.

## Version

This macro is used by the headers since SDL 3.0.0.

## See Also

* [SDL_AppInit](SDL_AppInit)
* [SDL_AppEvent](SDL_AppEvent)
* [SDL_AppIterate](SDL_AppIterate)
* [SDL_AppQuit](SDL_AppQuit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

