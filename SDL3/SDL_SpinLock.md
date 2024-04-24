###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SpinLock

An atomic spinlock.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
typedef int SDL_SpinLock;
```

## Remarks

The atomic locks are efficient spinlocks using CPU instructions, but are
vulnerable to starvation and can spin forever if a thread holding a lock
has been terminated. For this reason you should minimize the code executed
inside an atomic lock and never do expensive things like API or system
calls while holding them.

They are also vulnerable to starvation if the thread holding the lock is
lower priority than other threads and doesn't get scheduled. In general you
should use mutexes instead, since they have better performance and
contention behavior.

The atomic locks are not safe to lock recursively.

Porting Note: The spin lock functions and type are required and can not be
emulated because they are used in the atomic emulation code.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

