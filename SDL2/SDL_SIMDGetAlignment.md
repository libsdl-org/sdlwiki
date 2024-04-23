###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SIMDGetAlignment

Report the alignment this system needs for SIMD allocations.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h)

## Syntax

```c
size_t SDL_SIMDGetAlignment(void);

```

## Return Value

Returns the alignment in bytes needed for available, known SIMD
instructions.

## Remarks

This will return the minimum number of bytes to which a pointer must be
aligned to be compatible with SIMD instructions on the current machine. For
example, if the machine supports SSE only, it will return 16, but if it
supports AVX-512F, it'll return 64 (etc). This only reports values for
instruction sets SDL knows about, so if your SDL build doesn't have
[SDL_HasAVX512F](SDL_HasAVX512F)(), then it might return 16 for the SSE
support it sees and not 64 for the AVX-512 instructions that exist but SDL
doesn't know about. Plan accordingly.

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

