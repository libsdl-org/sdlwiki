###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SIMDGetAlignment

Report the alignment this system needs for SIMD allocations.

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_aligned_alloc](SDL_aligned_alloc)
* [SDL_aligned_free](SDL_aligned_free)

----
[CategoryAPI](CategoryAPI)

