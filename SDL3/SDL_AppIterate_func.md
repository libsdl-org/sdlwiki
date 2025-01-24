# SDL_AppIterate_func

Function pointer typedef for [SDL_AppIterate](SDL_AppIterate).

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
typedef SDL_AppResult (SDLCALL *SDL_AppIterate_func)(void *appstate);
```

## Function Parameters

|              |                                                                         |
| ------------ | ----------------------------------------------------------------------- |
| **appstate** | an optional pointer, provided by the app in [SDL_AppInit](SDL_AppInit). |

## Return Value

Returns [SDL_APP_FAILURE](SDL_APP_FAILURE) to terminate with an error,
[SDL_APP_SUCCESS](SDL_APP_SUCCESS) to terminate with success,
[SDL_APP_CONTINUE](SDL_APP_CONTINUE) to continue.

## Remarks

These are used by [SDL_EnterAppMainCallbacks](SDL_EnterAppMainCallbacks).
This mechanism operates behind the scenes for apps using the optional main
callbacks. Apps that want to use this should just implement
[SDL_AppIterate](SDL_AppIterate) directly.

## Version

This datatype is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryInit](CategoryInit)

