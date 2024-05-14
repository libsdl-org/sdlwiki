###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_atomic_t

A type representing an atomic integer value.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h)

## Syntax

```c
typedef struct SDL_atomic_t {
    int value;
} SDL_atomic_t;
```

## Remarks

It is a struct so people don't accidentally use numeric operations on it.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryAtomic](CategoryAtomic), [CategoryAPIStruct](CategoryAPIStruct), 

