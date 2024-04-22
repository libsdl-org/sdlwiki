###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LogGetPriority

Get the priority of a particular log category.

## Header File

Defined in [SDL_log.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_log.h)

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

This function is available since SDL 2.0.0.

## See Also

* [SDL_LogSetPriority](SDL_LogSetPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

