###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AppResult

Return values for optional main callbacks.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
typedef enum SDL_AppResult
{
    SDL_APP_CONTINUE,   /** Value that requests that the app continue from the main callbacks. */
    SDL_APP_SUCCESS,    /** Value that requests termination with success from the main callbacks. */
    SDL_APP_FAILURE     /** Value that requests termination with error from the main callbacks. */
} SDL_AppResult;
```

## Remarks

Returning [SDL_APP_SUCCESS](SDL_APP_SUCCESS) or
[SDL_APP_FAILURE](SDL_APP_FAILURE) from [SDL_AppInit](SDL_AppInit),
[SDL_AppEvent](SDL_AppEvent), or [SDL_AppIterate](SDL_AppIterate) will
terminate the program and report success/failure to the operating system.
What that means is platform-dependent. On Unix, for example, on success,
the process error code will be zero, and on failure it will be 1. This
interface doesn't allow you to return specific exit codes, just whether
there was an error generally or not.

Returning [SDL_APP_CONTINUE](SDL_APP_CONTINUE) from these functions will
let the app continue to run.

See
[Main callbacks in SDL3](https://wiki.libsdl.org/SDL3/README/main-functions#main-callbacks-in-sdl3)
for complete details.

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryInit](CategoryInit)

