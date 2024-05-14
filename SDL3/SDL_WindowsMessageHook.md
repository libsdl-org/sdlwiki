###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WindowsMessageHook

A callback to be used with [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook).

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
typedef SDL_bool (SDLCALL *SDL_WindowsMessageHook)(void *userdata, MSG *msg);
```

## Function Parameters

|                  |                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------- |
| **userdata**     | the app-defined pointer provided to [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook). |
| **msg**          | a pointer to a Win32 event structure to process.                                            |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) to let event continue on,
[SDL_FALSE](SDL_FALSE) to drop it.

## Remarks

This callback may modify the message, and should return
[SDL_TRUE](SDL_TRUE) if the message should continue to be processed, or
[SDL_FALSE](SDL_FALSE) to prevent further processing.

As this is processing a message directly from the Windows event loop, this
callback should do the minimum required work and return quickly.

## Thread Safety

This may only be called (by SDL) from the thread handling the Windows event
loop.

## Version

This datatype is available since SDL 3.0.0.

## Code Examples

```c
#if defined(SDL_PLATFORM_WIN32) || defined(SDL_PLATFORM_GDK)
SDL_bool MyMessageHook(void *userdata, MSG *msg)
{
    // do things with userdata and msg...

    return SDL_TRUE; // let SDL continue processing the message 
}

// ...
SDL_SetWindowsMessageHook(MyMessageHook, NULL);
#endif
```

## See Also

- [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook)
- [SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP](SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategorySystem](CategorySystem)

