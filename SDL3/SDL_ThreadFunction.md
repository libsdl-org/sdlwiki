###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitThread

The function passed to [SDL_CreateThread](https://wiki.libsdl.org/SDL3/SDL_CreateThread)()

## Syntax

```c
int SDL_ThreadFunction(void *data);

```

## Function Parameters

|                |                                                                                                                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **data**     | Data what was passed as *data* to [SDL_CreateThread](https://wiki.libsdl.org/SDL3/SDL_CreateThread)()         |


## Return Value

A value that can be reported through [SDL_WaitThread](https://wiki.libsdl.org/SDL3/SDL_WaitThread)()

## Remarks

See [SDL_CreateThread](https://wiki.libsdl.org/SDL3/SDL_CreateThread)() and [SDL_WaitThread](https://wiki.libsdl.org/SDL3/SDL_WaitThread)()

## Version

This function is available since SDL 3.0.0.

## Code Examples

See [SDL_WaitThread](https://wiki.libsdl.org/SDL3/SDL_WaitThread)()

## Related Functions

* [SDL_CreateThread](https://wiki.libsdl.org/SDL3/SDL_CreateThread)()
* [SDL_WaitThread](https://wiki.libsdl.org/SDL3/SDL_WaitThread)()

----
[CategoryAPI](CategoryAPI), [CategoryThread](CategoryThread)


