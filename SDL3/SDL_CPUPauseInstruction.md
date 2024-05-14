###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CPUPauseInstruction

A macro to insert a CPU-specific "pause" instruction into the program.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
#define SDL_CPUPauseInstruction() DoACPUPauseInACompilerAndArchitectureSpecificWay
```

## Remarks

This can be useful in busy-wait loops, as it serves as a hint to the CPU as
to the program's intent; some CPUs can use this to do more efficient
processing. On some platforms, this doesn't do anything, so using this
macro might just be a harmless no-op.

Note that if you are busy-waiting, there are often more-efficient
approaches with other synchronization primitives: mutexes, semaphores,
condition variables, etc.

## Thread Safety

This macro is safe to use from any thread.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAtomic](CategoryAtomic)

