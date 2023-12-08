###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetThreadName

Get the thread name as it was specified in [SDL_CreateThread](SDL_CreateThread.md)().

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
[SDL_WaitThread](SDL_WaitThread.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_CreateThread](SDL_CreateThread.md)

----
[CategoryAPI](CategoryAPI.md)
