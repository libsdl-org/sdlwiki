###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MemoryBarrierReleaseFunction

Insert a memory release barrier.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
void SDL_MemoryBarrierReleaseFunction(void);
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

## Thread Safety

Obviously this macro is safe to use from any thread at any time, but if you
find yourself needing this, you are probably dealing with some very
sensitive code; be careful!

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

