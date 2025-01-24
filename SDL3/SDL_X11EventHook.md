# SDL_X11EventHook

A callback to be used with [SDL_SetX11EventHook](SDL_SetX11EventHook).

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
typedef bool (SDLCALL *SDL_X11EventHook)(void *userdata, XEvent *xevent);
```

## Function Parameters

|              |                                                                                 |
| ------------ | ------------------------------------------------------------------------------- |
| **userdata** | the app-defined pointer provided to [SDL_SetX11EventHook](SDL_SetX11EventHook). |
| **xevent**   | a pointer to an Xlib XEvent union to process.                                   |

## Return Value

Returns true to let event continue on, false to drop it.

## Remarks

This callback may modify the event, and should return true if the event
should continue to be processed, or false to prevent further processing.

As this is processing an event directly from the X11 event loop, this
callback should do the minimum required work and return quickly.

## Thread Safety

This may only be called (by SDL) from the thread handling the X11 event
loop.

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_SetX11EventHook](SDL_SetX11EventHook)






----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySystem](CategorySystem)

