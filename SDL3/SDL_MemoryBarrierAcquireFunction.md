###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_MemoryBarrierAcquireFunction

Insert a memory acquire barrier.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
void SDL_MemoryBarrierAcquireFunction(void);
```

## Remarks

Please refer to
[SDL_MemoryBarrierReleaseFunction](SDL_MemoryBarrierReleaseFunction) for
the details!

## Thread Safety

Obviously this function is safe to use from any thread at any time, but if
you find yourself needing this, you are probably dealing with some very
sensitive code; be careful!

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_MemoryBarrierReleaseFunction](SDL_MemoryBarrierReleaseFunction)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

