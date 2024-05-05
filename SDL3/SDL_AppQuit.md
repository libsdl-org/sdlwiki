###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AppQuit

App-implemented deinit entry point for [SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS) apps.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
void SDL_AppQuit(void *appstate);

```

## Function Parameters

|                  |                                                                         |
| ---------------- | ----------------------------------------------------------------------- |
| **appstate**     | an optional pointer, provided by the app in [SDL_AppInit](SDL_AppInit). |

## Remarks

Apps implement this function when using
[SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS). If using a standard
"main" function, you should not supply this.

This function is called once by SDL before terminating the program.

This function will be called no matter what, even if
[SDL_AppInit](SDL_AppInit) requests termination.

This function should not go into an infinite mainloop; it should
deinitialize any resources necessary, perform whatever shutdown activities,
and return.

You do not need to call [SDL_Quit](SDL_Quit)() in this function, as SDL
will call it after this function returns and before the process terminates,
but it is safe to do so.

The `appstate` parameter is an optional pointer provided by the app during
[SDL_AppInit](SDL_AppInit)(). If the app never provided a pointer, this
will be NULL. This function call is the last time this pointer will be
provided, so any resources to it should be cleaned up here.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AppInit](SDL_AppInit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

