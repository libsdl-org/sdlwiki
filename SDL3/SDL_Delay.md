###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Delay

Wait a specified number of milliseconds before returning.

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
[CategoryAPI](CategoryAPI), [CategoryTimer](CategoryTimer)


