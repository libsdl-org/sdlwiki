###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_MainThreadCallback

Callback run on the main thread.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
typedef void (SDLCALL *SDL_MainThreadCallback)(void *userdata);
```

## Function Parameters

|              |                                                           |
| ------------ | --------------------------------------------------------- |
| **userdata** | an app-controlled pointer that is passed to the callback. |

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_RunOnMainThread](SDL_RunOnMainThread)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryInit](CategoryInit)

