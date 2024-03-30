###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

# SDL_WindowsMessageHook

A function definition to be used with [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook)

## Syntax

```c
#if defined(SDL_PLATFORM_WIN32) || defined(SDL_PLATFORM_GDK)
SDL_bool (*SDL_WindowsMessageHook)(void *userdata, MSG *msg);
#endif

```

## Definition Parameters

|              |                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------|
| **userdata** | the data passed by the original call to [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook)             |
| **msg**      | a pointer to a [MSG structure](https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-msg) |

## Remarks

This function may modify the message, and should return [SDL_TRUE](SDL_TRUE)
if the message should continue to be processed, or [SDL_FALSE](SDL_FALSE)
to prevent further processing.

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

## Version

This definition is available since SDL 3.0.0.

## Related Functions

* [SDL_SetWindowsMessageHook](SDL_SetWindowsMessageHook)

## Related Hints

* [SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP](SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP)

----
[CategoryDefine](CategoryDefine), [CategorySystem](CategorySystem)
