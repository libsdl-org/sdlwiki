# SDL_MemoryBarrierAcquire

Insert a memory acquire barrier (macro version).

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
#define SDL_MemoryBarrierAcquire() SDL_MemoryBarrierAcquireFunction()
```

## Remarks

Please see [SDL_MemoryBarrierRelease](SDL_MemoryBarrierRelease) for the
details on what memory barriers are and when to use them.

This is the macro version of this functionality; if possible, SDL will use
compiler intrinsics or inline assembly, but some platforms might need to
call the function version of this,
[SDL_MemoryBarrierAcquireFunction](SDL_MemoryBarrierAcquireFunction), to do
the heavy lifting. Apps that can use the macro should favor it over the
function.

## Thread Safety

Obviously this macro is safe to use from any thread at any time, but if you
find yourself needing this, you are probably dealing with some very
sensitive code; be careful!

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_MemoryBarrierRelease](SDL_MemoryBarrierRelease)
- [SDL_MemoryBarrierAcquireFunction](SDL_MemoryBarrierAcquireFunction)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAtomic](CategoryAtomic)

