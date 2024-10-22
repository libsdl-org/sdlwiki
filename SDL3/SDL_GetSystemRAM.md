###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetSystemRAM

Get the amount of RAM configured in the system.

## Header File

Defined in [<SDL3/SDL_cpuinfo.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_cpuinfo.h)

## Syntax

```c
int SDL_GetSystemRAM(void);
```

## Return Value

(int) Returns the amount of RAM configured in the system in MiB.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryCPUInfo](CategoryCPUInfo)

