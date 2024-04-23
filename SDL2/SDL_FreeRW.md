###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FreeRW

Use this function to free an [SDL_RWops](SDL_RWops) structure allocated by [SDL_AllocRW](SDL_AllocRW)().

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
void SDL_FreeRW(SDL_RWops * area);

```

## Function Parameters

|              |                                                  |
| ------------ | ------------------------------------------------ |
| **area**     | the [SDL_RWops](SDL_RWops) structure to be freed |

## Remarks

Applications do not need to use this function unless they are providing
their own [SDL_RWops](SDL_RWops) implementation. If you just need a
[SDL_RWops](SDL_RWops) to read/write a common data source, you should use
the built-in implementations in SDL, like
[SDL_RWFromFile](SDL_RWFromFile)() or [SDL_RWFromMem](SDL_RWFromMem)(),
etc, and call the **close** method on those [SDL_RWops](SDL_RWops) pointers
when you are done with them.

Only use [SDL_FreeRW](SDL_FreeRW)() on pointers returned by
[SDL_AllocRW](SDL_AllocRW)(). The pointer is invalid as soon as this
function returns. Any extra memory allocated during creation of the
[SDL_RWops](SDL_RWops) is not freed by [SDL_FreeRW](SDL_FreeRW)(); the
programmer must be responsible for managing that memory in their **close**
method.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AllocRW](SDL_AllocRW)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


