###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicInt

A type representing an atomic integer value.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef struct SDL_AtomicInt { int value; } SDL_AtomicInt;
```

## Remarks

It is a struct so people don't accidentally use numeric operations on it.

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

