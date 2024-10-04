###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_InitStatus

The current status of an [SDL_InitState](SDL_InitState) structure.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
typedef enum SDL_InitStatus
{
    SDL_INIT_STATUS_UNINITIALIZED,
    SDL_INIT_STATUS_INITIALIZING,
    SDL_INIT_STATUS_INITIALIZED,
    SDL_INIT_STATUS_UNINITIALIZING
} SDL_InitStatus;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryMutex](CategoryMutex)

