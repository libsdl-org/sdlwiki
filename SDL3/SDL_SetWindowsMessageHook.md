###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetWindowsMessageHook

Set a callback for every Windows message, run before TranslateMessage().

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
void SDL_SetWindowsMessageHook(SDL_WindowsMessageHook callback, void *userdata);
```

## Function Parameters

|                                                  |              |                                                                        |
| ------------------------------------------------ | ------------ | ---------------------------------------------------------------------- |
| [SDL_WindowsMessageHook](SDL_WindowsMessageHook) | **callback** | The [SDL_WindowsMessageHook](SDL_WindowsMessageHook) function to call. |
| void *                                           | **userdata** | a pointer to pass to every iteration of `callback`                     |

## Remarks

The callback may modify the message, and should return [SDL_TRUE](SDL_TRUE)
if the message should continue to be processed, or [SDL_FALSE](SDL_FALSE)
to prevent further processing.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_WindowsMessageHook](SDL_WindowsMessageHook)
- [SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP](SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

