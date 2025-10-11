# SDL_GetSystemPageSize

Report the size of a page of memory.

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
int SDL_GetSystemPageSize(void);
```

## Return Value

(int) Returns the size of a single page of memory, in bytes, or 0 if SDL
can't determine this information.

## Remarks

Different platforms might have different memory page sizes. In current
times, 4 kilobytes is not unusual, but newer systems are moving to larger
page sizes, and esoteric platforms might have any unexpected size.

Note that this function can return 0, which means SDL can't determine the
page size on this platform. It will _not_ set an error string to be
retrieved with [SDL_GetError](SDL_GetError)() in this case! In this case,
defaulting to 4096 is often a reasonable option.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

