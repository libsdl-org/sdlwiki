###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AppInit

App-implemented initial entry point for [SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS) apps.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
int SDL_AppInit(void **appstate, int argc, char *argv[]);
```

## Function Parameters

|                  |                                                                      |
| ---------------- | -------------------------------------------------------------------- |
| **appstate**     | a place where the app can optionally store a pointer for future use. |
| **argc**         | The standard ANSI C main's argc; number of elements in `argv`        |
| **argv**         | The standard ANSI C main's argv; array of command line arguments.    |

## Return Value

Returns [SDL_APP_FAILURE](SDL_APP_FAILURE) to terminate with an error,
[SDL_APP_SUCCESS](SDL_APP_SUCCESS) to terminate with success,
[SDL_APP_CONTINUE](SDL_APP_CONTINUE) to continue.

## Remarks

Apps implement this function when using
[SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS). If using a standard
"main" function, you should not supply this.

This function is called by SDL once, at startup. The function should
initialize whatever is necessary, possibly create windows and open audio
devices, etc. The `argc` and `argv` parameters work like they would with a
standard "main" function.

This function should not go into an infinite mainloop; it should do any
one-time setup it requires and then return.

The app may optionally assign a pointer to `*appstate`. This pointer will
be provided on every future call to the other entry points, to allow
application state to be preserved between functions without the app needing
to use a global variable. If this isn't set, the pointer will be NULL in
future entry points.

If this function returns [SDL_APP_CONTINUE](SDL_APP_CONTINUE), the app will
proceed to normal operation, and will begin receiving repeated calls to
[SDL_AppIterate](SDL_AppIterate) and [SDL_AppEvent](SDL_AppEvent) for the
life of the program. If this function returns
[SDL_APP_FAILURE](SDL_APP_FAILURE), SDL will call
[SDL_AppQuit](SDL_AppQuit) and terminate the process with an exit code that
reports an error to the platform. If it returns
[SDL_APP_SUCCESS](SDL_APP_SUCCESS), SDL calls [SDL_AppQuit](SDL_AppQuit)
and terminates with an exit code that reports success to the platform.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AppIterate](SDL_AppIterate)
- [SDL_AppEvent](SDL_AppEvent)
- [SDL_AppQuit](SDL_AppQuit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

