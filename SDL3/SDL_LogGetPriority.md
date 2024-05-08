###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LogGetPriority

Get the priority of a particular log category.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
SDL_LogPriority SDL_LogGetPriority(int category);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **category**     | the category to query |

## Return Value

Returns the [SDL_LogPriority](SDL_LogPriority) for the requested category

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_LogSetPriority](SDL_LogSetPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

