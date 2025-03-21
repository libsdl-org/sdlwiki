# SDL_SIMDAlloc

Allocate memory in a SIMD-friendly way.

## Header File

Defined in [SDL_cpuinfo.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_cpuinfo.h)

## Syntax

```c
void * SDL_SIMDAlloc(const size_t len);
```

## Function Parameters

|              |         |                                                                                                                 |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------- |
| const size_t | **len** | The length, in bytes, of the block to allocate. The actual allocated block might be larger due to padding, etc. |

## Return Value

(void *) Returns a pointer to the newly-allocated block, NULL if out of
memory.

## Remarks

This will allocate a block of memory that is suitable for use with SIMD
instructions. Specifically, it will be properly aligned and padded for the
system's supported vector instructions.

The memory returned will be padded such that it is safe to read or write an
incomplete vector at the end of the memory block. This can be useful so you
don't have to drop back to a scalar fallback at the end of your SIMD
processing loop to deal with the final elements without overflowing the
allocated buffer.

You must free this memory with [SDL_FreeSIMD](SDL_FreeSIMD)(), not free()
or [SDL_free](SDL_free)() or delete[], etc.

Note that SDL will only deal with SIMD instruction sets it is aware of; for
example, SDL 2.0.8 knows that SSE wants 16-byte vectors
([SDL_HasSSE](SDL_HasSSE)()), and AVX2 wants 32 bytes
([SDL_HasAVX2](SDL_HasAVX2)()), but doesn't know that AVX-512 wants 64. To
be clear: if you can't decide to use an instruction set with an
[SDL_Has](SDL_Has)*() function, don't use that instruction set with memory
allocated through here.

[SDL_AllocSIMD](SDL_AllocSIMD)(0) will return a non-NULL pointer, assuming
the system isn't out of memory, but you are not allowed to dereference it
(because you only own zero bytes of that buffer).

## Version

This function is available since SDL 2.0.10.

## See Also

- [SDL_SIMDGetAlignment](SDL_SIMDGetAlignment)
- [SDL_SIMDRealloc](SDL_SIMDRealloc)
- [SDL_SIMDFree](SDL_SIMDFree)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

