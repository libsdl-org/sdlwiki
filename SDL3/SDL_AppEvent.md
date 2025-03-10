# SDL_AppEvent

App-implemented event entry point for [SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS) apps.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
SDL_AppResult SDL_AppEvent(void *appstate, SDL_Event *event);
```

## Function Parameters

|                          |              |                                                                         |
| ------------------------ | ------------ | ----------------------------------------------------------------------- |
| void *                   | **appstate** | an optional pointer, provided by the app in [SDL_AppInit](SDL_AppInit). |
| [SDL_Event](SDL_Event) * | **event**    | the new event for the app to examine.                                   |

## Return Value

([SDL_AppResult](SDL_AppResult)) Returns [SDL_APP_FAILURE](SDL_APP_FAILURE)
to terminate with an error, [SDL_APP_SUCCESS](SDL_APP_SUCCESS) to terminate
with success, [SDL_APP_CONTINUE](SDL_APP_CONTINUE) to continue.

## Remarks

Apps implement this function when using
[SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS). If using a standard
"main" function, you should not supply this.

This function is called as needed by SDL after [SDL_AppInit](SDL_AppInit)
returns [SDL_APP_CONTINUE](SDL_APP_CONTINUE). It is called once for each
new event.

There is (currently) no guarantee about what thread this will be called
from; whatever thread pushes an event onto SDL's queue will trigger this
function. SDL is responsible for pumping the event queue between each call
to [SDL_AppIterate](SDL_AppIterate), so in normal operation one should only
get events in a serial fashion, but be careful if you have a thread that
explicitly calls [SDL_PushEvent](SDL_PushEvent). SDL itself will push
events to the queue on the main thread.

Events sent to this function are not owned by the app; if you need to save
the data, you should copy it.

This function should not go into an infinite mainloop; it should handle the
provided event appropriately and return.

The `appstate` parameter is an optional pointer provided by the app during
[SDL_AppInit](SDL_AppInit)(). If the app never provided a pointer, this
will be NULL.

If this function returns [SDL_APP_CONTINUE](SDL_APP_CONTINUE), the app will
continue normal operation, receiving repeated calls to
[SDL_AppIterate](SDL_AppIterate) and [SDL_AppEvent](SDL_AppEvent) for the
life of the program. If this function returns
[SDL_APP_FAILURE](SDL_APP_FAILURE), SDL will call
[SDL_AppQuit](SDL_AppQuit) and terminate the process with an exit code that
reports an error to the platform. If it returns
[SDL_APP_SUCCESS](SDL_APP_SUCCESS), SDL calls [SDL_AppQuit](SDL_AppQuit)
and terminates with an exit code that reports success to the platform.

## Thread Safety

This function may get called concurrently with
[SDL_AppIterate](SDL_AppIterate)() or [SDL_AppQuit](SDL_AppQuit)() for
events not pushed from the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AppInit](SDL_AppInit)
- [SDL_AppIterate](SDL_AppIterate)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

