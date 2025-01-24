# SDL_MemoryBarrierReleaseFunction

Insert a memory release barrier (function version).

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
void SDL_MemoryBarrierReleaseFunction(void);
```

## Remarks

Please refer to [SDL_MemoryBarrierRelease](SDL_MemoryBarrierRelease) for
details. This is a function version, which might be useful if you need to
use this functionality from a scripting language, etc. Also, some of the
macro versions call this function behind the scenes, where more heavy
lifting can happen inside of SDL. Generally, though, an app written in
C/C++/etc should use the macro version, as it will be more efficient.

## Thread Safety

Obviously this function is safe to use from any thread at any time, but if
you find yourself needing this, you are probably dealing with some very
sensitive code; be careful!

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_MemoryBarrierRelease](SDL_MemoryBarrierRelease)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

