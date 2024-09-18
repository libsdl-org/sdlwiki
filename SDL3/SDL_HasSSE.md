###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasSSE

Determine whether the CPU has SSE features.

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
bool SDL_HasSSE(void);
```

## Return Value

(bool) Returns true if the CPU has SSE features or false if not.

## Remarks

This always returns false on CPUs that aren't using Intel instruction sets.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_HasSSE2](SDL_HasSSE2)
- [SDL_HasSSE3](SDL_HasSSE3)
- [SDL_HasSSE41](SDL_HasSSE41)
- [SDL_HasSSE42](SDL_HasSSE42)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

