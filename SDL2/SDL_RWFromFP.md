###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWFromFP

Use this function to create an [SDL_RWops](SDL_RWops.md) structure from a standard I/O file pointer (stdio.h's `FILE*`).

## Syntax

```c
SDL_RWops* SDL_RWFromFP(void * fp,
                        SDL_bool autoclose);

```

## Function Parameters

|                   |                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **fp**            | the `FILE*` that feeds the [SDL_RWops](SDL_RWops.md) stream                                                                                                     |
| **autoclose**     | [SDL_TRUE](SDL_TRUE.md) to close the `FILE*` when closing the [SDL_RWops](SDL_RWops.md), [SDL_FALSE](SDL_FALSE.md) to leave the `FILE*` open when the RWops is closed |

## Return Value

Returns a pointer to the [SDL_RWops](SDL_RWops.md) structure that is created,
or NULL on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Remarks

This function is not available on Windows, since files opened in an
application on that platform cannot be used by a dynamically linked
library.

On some platforms, the first parameter is a `void*`, on others, it's a
`FILE*`, depending on what system headers are available to SDL. It is
always intended to be the `FILE*` type from the C runtime's stdio.h.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_RWclose](SDL_RWclose.md)
* [SDL_RWFromConstMem](SDL_RWFromConstMem.md)
* [SDL_RWFromFile](SDL_RWFromFile.md)
* [SDL_RWFromMem](SDL_RWFromMem.md)
* [SDL_RWread](SDL_RWread.md)
* [SDL_RWseek](SDL_RWseek.md)
* [SDL_RWtell](SDL_RWtell.md)
* [SDL_RWwrite](SDL_RWwrite.md)

----
[CategoryAPI](CategoryAPI.md)
