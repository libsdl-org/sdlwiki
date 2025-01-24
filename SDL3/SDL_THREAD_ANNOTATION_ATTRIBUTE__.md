# SDL_THREAD_ANNOTATION_ATTRIBUTE__

Enable thread safety attributes, only with clang.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
#define SDL_THREAD_ANNOTATION_ATTRIBUTE__(x)   __attribute__((x))
```

## Remarks

The attributes can be safely erased when compiling with other compilers.

To enable analysis, set these environment variables before running cmake:

```bash
export CC=clang
export CFLAGS="-DSDL_THREAD_SAFETY_ANALYSIS -Wthread-safety"
```

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryMutex](CategoryMutex)

