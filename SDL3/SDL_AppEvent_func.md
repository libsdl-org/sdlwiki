# SDL_AppEvent_func

Function pointer typedef for [SDL_AppEvent](SDL_AppEvent).

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
typedef SDL_AppResult (SDLCALL *SDL_AppEvent_func)(void *appstate, SDL_Event *event);
```

## Function Parameters

|              |                                                                         |
| ------------ | ----------------------------------------------------------------------- |
| **appstate** | an optional pointer, provided by the app in [SDL_AppInit](SDL_AppInit). |
| **event**    | the new event for the app to examine.                                   |

## Return Value

Returns [SDL_APP_FAILURE](SDL_APP_FAILURE) to terminate with an error,
[SDL_APP_SUCCESS](SDL_APP_SUCCESS) to terminate with success,
[SDL_APP_CONTINUE](SDL_APP_CONTINUE) to continue.

## Remarks

These are used by [SDL_EnterAppMainCallbacks](SDL_EnterAppMainCallbacks).
This mechanism operates behind the scenes for apps using the optional main
callbacks. Apps that want to use this should just implement
[SDL_AppEvent](SDL_AppEvent) directly.

## Version

This datatype is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryInit](CategoryInit)

