###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AppIterate

App-implemented iteration entry point for [SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS) apps.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
int SDL_AppIterate(void *appstate);

```

## Function Parameters

|                  |                                                                         |
| ---------------- | ----------------------------------------------------------------------- |
| **appstate**     | an optional pointer, provided by the app in [SDL_AppInit](SDL_AppInit). |

## Return Value

Returns [SDL_MAIN_CALLBACK_EXIT_FAILURE](SDL_MAIN_CALLBACK_EXIT_FAILURE) to
terminate with an error,
[SDL_MAIN_CALLBACK_EXIT_SUCCESS](SDL_MAIN_CALLBACK_EXIT_SUCCESS) to
terminate with success,
[SDL_MAIN_CALLBACK_CONTINUE](SDL_MAIN_CALLBACK_CONTINUE) to continue.

## Remarks

Apps implement this function when using
[SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS). If using a standard
"main" function, you should not supply this.

This function is called repeatedly by SDL after [SDL_AppInit](SDL_AppInit)
returns 0. The function should operate as a single iteration the program's
primary loop; it should update whatever state it needs and draw a new frame
of video, usually.

On some platforms, this function will be called at the refresh rate of the
display (which might change during the life of your app!). There are no
promises made about what frequency this function might run at. You should
use SDL's timer functions if you need to see how much time has passed since
the last iteration.

There is no need to process the SDL event queue during this function; SDL
will send events as they arrive in [SDL_AppEvent](SDL_AppEvent), and in
most cases the event queue will be empty when this function runs anyhow.

This function should not go into an infinite mainloop; it should do one
iteration of whatever the program does and return.

The `appstate` parameter is an optional pointer provided by the app during
[SDL_AppInit](SDL_AppInit)(). If the app never provided a pointer, this
will be NULL.

If this function returns
[SDL_MAIN_CALLBACK_CONTINUE](SDL_MAIN_CALLBACK_CONTINUE), the app will
continue normal operation, receiving repeated calls to
[SDL_AppIterate](SDL_AppIterate) and [SDL_AppEvent](SDL_AppEvent) for the
life of the program. If this function returns
[SDL_MAIN_CALLBACK_EXIT_FAILURE](SDL_MAIN_CALLBACK_EXIT_FAILURE), SDL will
call [SDL_AppQuit](SDL_AppQuit) and terminate the process with an exit code
that reports an error to the platform. If it returns
[SDL_MAIN_CALLBACK_EXIT_SUCCESS](SDL_MAIN_CALLBACK_EXIT_SUCCESS), SDL calls
[SDL_AppQuit](SDL_AppQuit) and terminates with an exit code that reports
success to the platform.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AppInit](SDL_AppInit)
- [SDL_AppEvent](SDL_AppEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

