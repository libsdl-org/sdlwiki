###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetThreadName

Get the thread name as it was specified in [SDL_CreateThread](SDL_CreateThread)().

## Header File

Defined in [<SDL3/SDL_thread.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_thread.h)

## Syntax

```c
const char* SDL_GetThreadName(SDL_Thread *thread);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **thread**     | the thread to query |

## Return Value

Returns a pointer to a UTF-8 string that names the specified thread, or
NULL if it doesn't have a name.

## Remarks

This is internal memory, not to be freed by the caller, and remains valid
until the specified thread is cleaned up by
[SDL_WaitThread](SDL_WaitThread)().

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

