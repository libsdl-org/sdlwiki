###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TimeFromWindows

Converts a Windows FILETIME (100-nanosecond intervals since January 1, 1601) to an SDL time.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
SDL_Time SDL_TimeFromWindows(Uint32 dwLowDateTime, Uint32 dwHighDateTime);
```

## Function Parameters

|        |                    |                                                 |
| ------ | ------------------ | ----------------------------------------------- |
| Uint32 | **dwLowDateTime**  | the low portion of the Windows FILETIME value.  |
| Uint32 | **dwHighDateTime** | the high portion of the Windows FILETIME value. |

## Return Value

([SDL_Time](SDL_Time)) Returns the converted SDL time.

## Remarks

This function takes the two 32-bit values of the FILETIME structure as
parameters.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTime](CategoryTime)

