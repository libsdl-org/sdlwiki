###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LogGetOutputFunction

Get the current log output function.

## Syntax

```c
void SDL_LogGetOutputFunction(SDL_LogOutputFunction *callback, void **userdata);

```

## Function Parameters

|                  |                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------- |
| **callback**     | an [SDL_LogOutputFunction](SDL_LogOutputFunction) filled in with the current log callback |
| **userdata**     | a pointer filled in with the pointer that is passed to `callback`                         |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LogSetOutputFunction](SDL_LogSetOutputFunction)

----
[CategoryAPI](CategoryAPI), [CategoryLog](CategoryLog)


