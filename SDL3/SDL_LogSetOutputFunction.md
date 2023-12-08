###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LogSetOutputFunction

Replace the default log output function with one of your own.

## Syntax

```c
void SDL_LogSetOutputFunction(SDL_LogOutputFunction callback, void *userdata);

```

## Function Parameters

|                  |                                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| **callback**     | an [SDL_LogOutputFunction](SDL_LogOutputFunction.md) to call instead of the default |
| **userdata**     | a pointer that is passed to `callback`                                           |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LogGetOutputFunction](SDL_LogGetOutputFunction.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryLog](CategoryLog.md)
