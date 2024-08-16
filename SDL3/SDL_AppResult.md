###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AppResult

Return values for optional main callbacks.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
typedef enum SDL_AppResult
{
    SDL_APP_CONTINUE,   /** Value that requests that the app continue from the main callbacks. If SDL_AppInit, SDL_AppEvent, or SDL_AppIterate returns this value, the program will continue to run. */
    SDL_APP_SUCCESS,    /** Value that requests termination with success from the main callbacks. If SDL_AppInit, SDL_AppEvent, or SDL_AppIterate returns this value, the program will terminate and report success to the operating system. What that success looks like is platform-dependent. On Unix, for example, the process error code will be zero. */
    SDL_APP_FAILURE     /** Value that requests termination with error from the main callbacks. If SDL_AppInit, SDL_AppEvent, or SDL_AppIterate returns this value, the program will terminate and report failure to the operating system. What that failure looks like is platform-dependent. On Unix, for example, the process error code will be non-zero. */
} SDL_AppResult;
```

## Remarks

See
https://wiki.libsdl.org/SDL3/README/main-functions#main-callbacks-in-sdl3
for details.

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryInit](CategoryInit)

