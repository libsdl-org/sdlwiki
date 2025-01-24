# SDL_SetX11EventHook

Set a callback for every X11 event.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
void SDL_SetX11EventHook(SDL_X11EventHook callback, void *userdata);
```

## Function Parameters

|                                      |              |                                                            |
| ------------------------------------ | ------------ | ---------------------------------------------------------- |
| [SDL_X11EventHook](SDL_X11EventHook) | **callback** | the [SDL_X11EventHook](SDL_X11EventHook) function to call. |
| void *                               | **userdata** | a pointer to pass to every iteration of `callback`.        |

## Remarks

The callback may modify the event, and should return true if the event
should continue to be processed, or false to prevent further processing.

## Version

This function is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

