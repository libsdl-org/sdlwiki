###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_AppInit_func

Function pointer typedef for [SDL_AppInit](SDL_AppInit).

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
typedef SDL_AppResult (SDLCALL *SDL_AppInit_func)(void **appstate, int argc, char *argv[]);
```

## Function Parameters

|              |                                                                      |
| ------------ | -------------------------------------------------------------------- |
| **appstate** | a place where the app can optionally store a pointer for future use. |
| **argc**     | the standard ANSI C main's argc; number of elements in `argv`.       |
| **argv**     | the standard ANSI C main's argv; array of command line arguments.    |

## Return Value

Returns [SDL_APP_FAILURE](SDL_APP_FAILURE) to terminate with an error,
[SDL_APP_SUCCESS](SDL_APP_SUCCESS) to terminate with success,
[SDL_APP_CONTINUE](SDL_APP_CONTINUE) to continue.

## Remarks

These are used by [SDL_EnterAppMainCallbacks](SDL_EnterAppMainCallbacks).
This mechanism operates behind the scenes for apps using the optional main
callbacks. Apps that want to use this should just implement
[SDL_AppInit](SDL_AppInit) directly.

## Version

This datatype is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryInit](CategoryInit)

