###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWFromFP

Use this function to create an [SDL_RWops](SDL_RWops) structure from a standard I/O file pointer (stdio.h's `FILE*`).

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
SDL_RWops* SDL_RWFromFP(void * fp,
                    SDL_bool autoclose);
```

## Function Parameters

|                      |               |                                                                                                                                                              |
| -------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| void *               | **fp**        | the `FILE*` that feeds the [SDL_RWops](SDL_RWops) stream                                                                                                     |
| [SDL_bool](SDL_bool) | **autoclose** | [SDL_TRUE](SDL_TRUE) to close the `FILE*` when closing the [SDL_RWops](SDL_RWops), [SDL_FALSE](SDL_FALSE) to leave the `FILE*` open when the RWops is closed |

## Return Value

([SDL_RWops](SDL_RWops) *) Returns a pointer to the [SDL_RWops](SDL_RWops)
structure that is created, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function is not available on Windows, since files opened in an
application on that platform cannot be used by a dynamically linked
library.

On some platforms, the first parameter is a `void*`, on others, it's a
`FILE*`, depending on what system headers are available to SDL. It is
always intended to be the `FILE*` type from the C runtime's stdio.h.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_RWclose](SDL_RWclose)
- [SDL_RWFromConstMem](SDL_RWFromConstMem)
- [SDL_RWFromFile](SDL_RWFromFile)
- [SDL_RWFromMem](SDL_RWFromMem)
- [SDL_RWread](SDL_RWread)
- [SDL_RWseek](SDL_RWseek)
- [SDL_RWtell](SDL_RWtell)
- [SDL_RWwrite](SDL_RWwrite)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRWOPS](CategoryRWOPS)

