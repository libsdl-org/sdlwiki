###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ThreadFunction

The function passed to [SDL_CreateThread](SDL_CreateThread)().

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
typedef int (SDLCALL * SDL_ThreadFunction) (void *data);
```

## Function Parameters

|              |                                                                     |
| ------------ | ------------------------------------------------------------------- |
| **data**     | what was passed as `data` to [SDL_CreateThread](SDL_CreateThread)() |

## Return Value

Returns a value that can be reported through
[SDL_WaitThread](SDL_WaitThread)().

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

