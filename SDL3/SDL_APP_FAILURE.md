###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_APP_FAILURE

Value that requests termination with error from the main callbacks.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
#define SDL_APP_FAILURE -1
```

## Remarks

If [SDL_AppInit](SDL_AppInit), [SDL_AppEvent](SDL_AppEvent), or
[SDL_AppIterate](SDL_AppIterate) returns this value, the program will
terminate and report failure to the operating system.

What that failure looks like is platform-dependent. On Unix, for example,
the process error code will be non-zero.

This is always -1; using this macro may be clearer, but is not required.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMain](CategoryMain)

