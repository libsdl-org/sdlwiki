# SDL_AtomicU32

A type representing an atomic unsigned 32-bit value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
typedef struct SDL_AtomicU32 { Uint32 value; } SDL_AtomicU32;
```

## Remarks

This can be used to manage a value that is synchronized across multiple
CPUs without a race condition; when an app sets a value with
[SDL_SetAtomicU32](SDL_SetAtomicU32) all other threads, regardless of the
CPU it is running on, will see that value when retrieved with
[SDL_GetAtomicU32](SDL_GetAtomicU32), regardless of CPU caches, etc.

This is also useful for atomic compare-and-swap operations: a thread can
change the value as long as its current value matches expectations. When
done in a loop, one can guarantee data consistency across threads without a
lock (but the usual warnings apply: if you don't know what you're doing, or
you don't do it carefully, you can confidently cause any number of
disasters with this, so in most cases, you _should_ use a mutex instead of
this!).

This is a struct so people don't accidentally use numeric operations on it
directly. You have to use SDL atomic functions.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_CompareAndSwapAtomicU32](SDL_CompareAndSwapAtomicU32)
- [SDL_GetAtomicU32](SDL_GetAtomicU32)
- [SDL_SetAtomicU32](SDL_SetAtomicU32)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryAtomic](CategoryAtomic)

