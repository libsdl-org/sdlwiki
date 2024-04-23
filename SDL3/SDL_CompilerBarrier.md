###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CompilerBarrier

Mark a compiler barrier.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
#define SDL_CompilerBarrier() DoCompilerSpecificReadWriteBarrier()
```

## Remarks

A compiler barrier prevents the compiler from reordering reads and writes
to globally visible variables across the call.

This macro only prevents the compiler from reordering reads and writes, it
does not prevent the CPU from reordering reads and writes. However, all of
the atomic operations that modify memory are full memory barriers.

## Thread Safety

Obviously this macro is safe to use from any thread at any time, but if you
find yourself needing this, you are probably dealing with some very
sensitive code; be careful!

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

