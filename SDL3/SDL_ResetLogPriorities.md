###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ResetLogPriorities

Reset all priorities to default.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
void SDL_ResetLogPriorities(void);

```

## Remarks

This is called by [SDL_Quit](SDL_Quit)().

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetLogPriorities](SDL_SetLogPriorities)
- [SDL_SetLogPriority](SDL_SetLogPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

