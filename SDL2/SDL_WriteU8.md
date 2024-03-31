###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WriteU8

Use this function to write a byte to an [SDL_RWops](SDL_RWops).

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
size_t SDL_WriteU8(SDL_RWops * dst, Uint8 value);

```

## Function Parameters

|               |                                        |
| ------------- | -------------------------------------- |
| **dst**       | the [SDL_RWops](SDL_RWops) to write to |
| **value**     | the byte value to write                |

## Return Value

Returns 1 on success or 0 on failure; call [SDL_GetError](SDL_GetError)()
for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_ReadU8](SDL_ReadU8)

----
[CategoryAPI](CategoryAPI)

