###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ReadU8

Use this function to read a byte from an [SDL_RWops](SDL_RWops).

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
Uint8 SDL_ReadU8(SDL_RWops * src);

```

## Function Parameters

|             |                                         |
| ----------- | --------------------------------------- |
| **src**     | the [SDL_RWops](SDL_RWops) to read from |

## Return Value

Returns the read byte on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_WriteU8](SDL_WriteU8)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

