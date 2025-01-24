# SDL_MemoryBarrierRelease

Insert a memory release barrier (macro version).

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
#define SDL_MemoryBarrierRelease() SDL_MemoryBarrierReleaseFunction()
```

## Remarks

Memory barriers are designed to prevent reads and writes from being
reordered by the compiler and being seen out of order on multi-core CPUs.

A typical pattern would be for thread A to write some data and a flag, and
for thread B to read the flag and get the data. In this case you would
insert a release barrier between writing the data and the flag,
guaranteeing that the data write completes no later than the flag is
written, and you would insert an acquire barrier between reading the flag
and reading the data, to ensure that all the reads associated with the flag
have completed.

In this pattern you should always see a release barrier paired with an
acquire barrier and you should gate the data reads/writes with a single
flag variable.

For more information on these semantics, take a look at the blog post:
http://preshing.com/20120913/acquire-and-release-semantics

This is the macro version of this functionality; if possible, SDL will use
compiler intrinsics or inline assembly, but some platforms might need to
call the function version of this,
[SDL_MemoryBarrierReleaseFunction](SDL_MemoryBarrierReleaseFunction) to do
the heavy lifting. Apps that can use the macro should favor it over the
function.

## Thread Safety

Obviously this macro is safe to use from any thread at any time, but if you
find yourself needing this, you are probably dealing with some very
sensitive code; be careful!

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_MemoryBarrierAcquire](SDL_MemoryBarrierAcquire)
- [SDL_MemoryBarrierReleaseFunction](SDL_MemoryBarrierReleaseFunction)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAtomic](CategoryAtomic)

