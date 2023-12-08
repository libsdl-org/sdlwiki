###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyRW

Use this function to free an [SDL_RWops](SDL_RWops.md) structure allocated by [SDL_CreateRW](SDL_CreateRW.md)().

## Syntax

```c
void SDL_DestroyRW(SDL_RWops *context);

```

## Function Parameters

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **context**     | the [SDL_RWops](SDL_RWops.md) structure to be freed |

## Remarks

Applications do not need to use this function unless they are providing
their own [SDL_RWops](SDL_RWops.md) implementation. If you just need an
[SDL_RWops](SDL_RWops.md) to read/write a common data source, you should use
the built-in implementations in SDL, like
[SDL_RWFromFile](SDL_RWFromFile.md)() or [SDL_RWFromMem](SDL_RWFromMem.md)(),
etc, and call the **close** method on those [SDL_RWops](SDL_RWops.md) pointers
when you are done with them.

Only use [SDL_DestroyRW](SDL_DestroyRW.md)() on pointers returned by
[SDL_CreateRW](SDL_CreateRW.md)(). The pointer is invalid as soon as this
function returns. Any extra memory allocated during creation of the
[SDL_RWops](SDL_RWops.md) is not freed by [SDL_DestroyRW](SDL_DestroyRW.md)();
the programmer must be responsible for managing that memory in their
**close** method.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreateRW](SDL_CreateRW.md)

----
[CategoryAPI](CategoryAPI.md)
