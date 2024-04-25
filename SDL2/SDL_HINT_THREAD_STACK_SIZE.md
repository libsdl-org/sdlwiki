###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_THREAD_STACK_SIZE

A string specifying SDL's threads stack size in bytes or "0" for the backend's default size

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_THREAD_STACK_SIZE              "SDL_THREAD_STACK_SIZE"
```

## Remarks

Use this hint in case you need to set SDL's threads stack size to other
than the default. This is specially useful if you build SDL against a non
glibc libc library (such as musl) which provides a relatively small default
thread stack size (a few kilobytes versus the default 8MB glibc uses).
Support for this hint is currently available only in the pthread, Windows,
and PSP backend.

Instead of this hint, in 2.0.9 and later, you can use
[SDL_CreateThreadWithStackSize](SDL_CreateThreadWithStackSize)(). This hint
only works with the classic [SDL_CreateThread](SDL_CreateThread)().

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)


