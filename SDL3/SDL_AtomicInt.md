###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicInt

A type representing an atomic integer value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
typedef struct SDL_AtomicInt { int value; } SDL_AtomicInt;
```

## Remarks

This can be used to manage a value that is synchronized across multiple
CPUs without a race condition; when an app sets a value with
[SDL_AtomicSet](SDL_AtomicSet) all other threads, regardless of the CPU it
is running on, will see that value when retrieved with
[SDL_AtomicGet](SDL_AtomicGet), regardless of CPU caches, etc.

This is also useful for atomic compare-and-swap operations: a thread can
change the value as long as its current value matches expectations. When
done in a loop, one can guarantee data consistency across threads without a
lock (but the usual warnings apply: if you don't know what you're doing, or
you don't do it carefully, you can confidently cause any number of
disasters with this, so in most cases, you _should_ use a mutex instead of
this!).

This is a struct so people don't accidentally use numeric operations on it
directly. You have to use [SDL_Atomic](SDL_Atomic)* functions.

## Version

This struct is available since SDL 3.0.0.

## See Also

- [SDL_AtomicCompareAndSwap](SDL_AtomicCompareAndSwap)
- [SDL_AtomicGet](SDL_AtomicGet)
- [SDL_AtomicSet](SDL_AtomicSet)
- [SDL_AtomicAdd](SDL_AtomicAdd)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

