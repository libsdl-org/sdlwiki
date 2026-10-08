# SDL_AppQuit

App-implemented deinit entry point for [SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS) apps.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
void SDL_AppQuit(void *appstate, SDL_AppResult result);
```

## Function Parameters

|                                |              |                                                                         |
| ------------------------------ | ------------ | ----------------------------------------------------------------------- |
| void *                         | **appstate** | an optional pointer, provided by the app in [SDL_AppInit](SDL_AppInit). |
| [SDL_AppResult](SDL_AppResult) | **result**   | the result code that terminated the app (success or failure).           |

## Remarks

Apps implement this function when using
[SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS). If using a standard
"main" function, you should not supply this.

This function is called once by SDL before terminating the program.

This function will be called in all normal cases, even if
[SDL_AppInit](SDL_AppInit) requests termination at startup. This function
will not be called for abnormal process termination, such as a segfault or
other crash.

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

This function is called by SDL on the main thread.

Note that as of SDL 3.6.0, on mobile platforms, this function will be
called if the system is terminating the app mid-run. In this case, `result`
will be set to [SDL_APP_CONTINUE](SDL_APP_CONTINUE) to signify that this
was not the app requesting termination due to either a successful or failed
run. This operates as an alternative to registering an event watcher to
monitor for [SDL_EVENT_TERMINATING](SDL_EVENT_TERMINATING), if the app is
using the main callbacks anyway.

## Thread Safety

[SDL_AppEvent](SDL_AppEvent)() may get called concurrently with this
function if other threads that push events are still active.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AppInit](SDL_AppInit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

