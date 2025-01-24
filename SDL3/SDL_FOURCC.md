# SDL_FOURCC

Define a four character code as a [Uint32](Uint32).

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_FOURCC(A, B, C, D) \
    ((SDL_static_cast(Uint32, SDL_static_cast(Uint8, (A))) << 0) | \
     (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (B))) << 8) | \
     (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (C))) << 16) | \
     (SDL_static_cast(Uint32, SDL_static_cast(Uint8, (D))) << 24))
```

## Macro Parameters

|       |                             |
| ----- | --------------------------- |
| **A** | the first ASCII character.  |
| **B** | the second ASCII character. |
| **C** | the third ASCII character.  |
| **D** | the fourth ASCII character. |

## Return Value

Returns the four characters converted into a [Uint32](Uint32), one
character per-byte.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

