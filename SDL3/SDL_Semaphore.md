###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Semaphore

A means to manage access to a resource, by count, between threads.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
typedef struct SDL_Semaphore SDL_Semaphore;
```

## Remarks

Semaphores (specifically, "counting semaphores"), let X number of threads
request access at the same time, each thread granted access decrementing a
counter. When the counter reaches zero, future requests block until a prior
thread releases their request, incrementing the counter again.

Wikipedia has a thorough explanation of the concept:

https://en.wikipedia.org/wiki/Semaphore_(programming)

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

