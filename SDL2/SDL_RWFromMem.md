###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWFromMem

Use this function to prepare a read-write memory buffer for use with [SDL_RWops](SDL_RWops).

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_RWops* SDL_RWFromMem(void *mem, int size);

```

## Function Parameters

|              |                                                                |
| ------------ | -------------------------------------------------------------- |
| **mem**      | a pointer to a buffer to feed an [SDL_RWops](SDL_RWops) stream |
| **size**     | the buffer size, in bytes                                      |

## Return Value

Returns a pointer to a new [SDL_RWops](SDL_RWops) structure, or NULL if it
fails; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function sets up an [SDL_RWops](SDL_RWops) struct based on a memory
area of a certain size, for both read and write access.

This memory buffer is not copied by the RWops; the pointer you provide must
remain valid until you close the stream. Closing the stream will not free
the original buffer.

If you need to make sure the RWops never writes to the memory buffer, you
should use [SDL_RWFromConstMem](SDL_RWFromConstMem)() with a read-only
buffer of memory instead.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_RWclose](SDL_RWclose)
* [SDL_RWFromConstMem](SDL_RWFromConstMem)
* [SDL_RWFromFile](SDL_RWFromFile)
* [SDL_RWFromFP](SDL_RWFromFP)
* [SDL_RWFromMem](SDL_RWFromMem)
* [SDL_RWread](SDL_RWread)
* [SDL_RWseek](SDL_RWseek)
* [SDL_RWtell](SDL_RWtell)
* [SDL_RWwrite](SDL_RWwrite)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

