###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LogSetOutputFunction

Replace the default log output function with one of your own.

## Header File

Defined in [SDL_log.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_log.h)

## Syntax

```c
void SDL_LogSetOutputFunction(SDL_LogOutputFunction callback, void *userdata);

```

## Function Parameters

|                  |                                                                                  |
| ---------------- | -------------------------------------------------------------------------------- |
| **callback**     | an [SDL_LogOutputFunction](SDL_LogOutputFunction) to call instead of the default |
| **userdata**     | a pointer that is passed to `callback`                                           |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_LogGetOutputFunction](SDL_LogGetOutputFunction)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

