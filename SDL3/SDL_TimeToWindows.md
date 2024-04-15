###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TimeToWindows

Converts an SDL time into a Windows FILETIME (100-nanosecond intervals since January 1, 1601).

## Header File

Defined in [SDL_time.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
void SDL_TimeToWindows(SDL_Time ticks, Uint32 *dwLowDateTime, Uint32 *dwHighDateTime);

```

## Function Parameters

|                        |                                                                         |
| ---------------------- | ----------------------------------------------------------------------- |
| **ticks**              | the time to convert                                                     |
| **dwLowDateTime**      | a pointer filled in with the low portion of the Windows FILETIME value  |
| **dwHighDateTime**     | a pointer filled in with the high portion of the Windows FILETIME value |

## Remarks

This function fills in the two 32-bit values of the FILETIME structure.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

