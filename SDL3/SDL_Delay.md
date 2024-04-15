###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Delay

Wait a specified number of milliseconds before returning.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
void SDL_Delay(Uint32 ms);

```

## Function Parameters

|            |                                     |
| ---------- | ----------------------------------- |
| **ms**     | the number of milliseconds to delay |

## Remarks

This function waits a specified number of milliseconds before returning. It
waits at least the specified time, but possibly longer due to OS
scheduling.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)


