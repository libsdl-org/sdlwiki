###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PLATFORM_LINUX

A preprocessor macro that is only defined if compiling for Linux.

## Header File

Defined in [<SDL3/SDL_platform_defines.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_platform_defines.h)

## Syntax

```c
#define SDL_PLATFORM_LINUX 1
```

## Remarks

Note that Android, although ostensibly a Linux-based system, will not
define this. It defines [SDL_PLATFORM_ANDROID](SDL_PLATFORM_ANDROID)
instead.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPlatform](CategoryPlatform)

