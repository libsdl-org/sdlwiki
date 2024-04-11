###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AllocRW

Use this function to allocate an empty, unpopulated [SDL_RWops](SDL_RWops) structure.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_RWops* SDL_AllocRW(void);

```

## Return Value

Returns a pointer to the allocated memory on success, or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Applications do not need to use this function unless they are providing
their own [SDL_RWops](SDL_RWops) implementation. If you just need a
[SDL_RWops](SDL_RWops) to read/write a common data source, you should use
the built-in implementations in SDL, like
[SDL_RWFromFile](SDL_RWFromFile)() or [SDL_RWFromMem](SDL_RWFromMem)(),
etc.

You must free the returned pointer with [SDL_FreeRW](SDL_FreeRW)().
Depending on your operating system and compiler, there may be a difference
between the malloc() and free() your program uses and the versions SDL
calls internally. Trying to mix the two can cause crashing such as
segmentation faults. Since all [SDL_RWops](SDL_RWops) must free themselves
when their **close** method is called, all [SDL_RWops](SDL_RWops) must be
allocated through this function, so they can all be freed correctly with
[SDL_FreeRW](SDL_FreeRW)().

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_FreeRW](SDL_FreeRW)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

