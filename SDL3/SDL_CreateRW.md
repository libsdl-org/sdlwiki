###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateRW

Use this function to allocate an empty, unpopulated [SDL_RWops](SDL_RWops) structure.

## Syntax

```c
SDL_RWops* SDL_CreateRW(void);

```

## Return Value

Returns a pointer to the allocated memory on success, or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Applications do not need to use this function unless they are providing
their own [SDL_RWops](SDL_RWops) implementation. If you just need an
[SDL_RWops](SDL_RWops) to read/write a common data source, you should use
the built-in implementations in SDL, like
[SDL_RWFromFile](SDL_RWFromFile)() or [SDL_RWFromMem](SDL_RWFromMem)(),
etc.

You must free the returned pointer with [SDL_DestroyRW](SDL_DestroyRW)().
Depending on your operating system and compiler, there may be a difference
between the malloc() and free() your program uses and the versions SDL
calls internally. Trying to mix the two can cause crashing such as
segmentation faults. Since all [SDL_RWops](SDL_RWops) must free themselves
when their **close** method is called, all [SDL_RWops](SDL_RWops) must be
allocated through this function, so they can all be freed correctly with
[SDL_DestroyRW](SDL_DestroyRW)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_DestroyRW](SDL_DestroyRW)

----
[CategoryAPI](CategoryAPI)

