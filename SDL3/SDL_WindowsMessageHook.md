# SDL_WindowsMessageHook

A callback to be used with [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook).

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
typedef bool (SDLCALL *SDL_WindowsMessageHook)(void *userdata, MSG *msg);
```

## Function Parameters

|              |                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------- |
| **userdata** | the app-defined pointer provided to [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook). |
| **msg**      | a pointer to a Win32 event structure to process.                                            |

## Return Value

Returns true to let event continue on, false to drop it.

## Remarks

This callback may modify the message, and should return true if the message
should continue to be processed, or false to prevent further processing.

As this is processing a message directly from the Windows event loop, this
callback should do the minimum required work and return quickly.

## Thread Safety

This may only be called (by SDL) from the thread handling the Windows event
loop.

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook)
- [SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP](SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySystem](CategorySystem)

