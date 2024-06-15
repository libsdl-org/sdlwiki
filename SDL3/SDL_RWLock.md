###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RWLock

A mutex that allows read-only threads to run in parallel.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
typedef struct SDL_RWLock SDL_RWLock;
```

## Remarks

A rwlock is roughly the same concept as [SDL_Mutex](SDL_Mutex), but allows
threads that request read-only access to all hold the lock at the same
time. If a thread requests write access, it will block until all read-only
threads have released the lock, and no one else can hold the thread (for
reading or writing) at the same time as the writing thread.

This can be more efficient in cases where several threads need to access
data frequently, but changes to that data are rare.

There are other rules that apply to rwlocks that don't apply to mutexes,
about how threads are scheduled and when they can be recursively locked.
These are documented in the other rwlock functions.

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryMutex](CategoryMutex)

