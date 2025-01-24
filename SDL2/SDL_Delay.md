# SDL_Delay

Wait a specified number of milliseconds before returning.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h)

## Syntax

```c
void SDL_Delay(Uint32 ms);
```

## Function Parameters

|                  |        |                                      |
| ---------------- | ------ | ------------------------------------ |
| [Uint32](Uint32) | **ms** | the number of milliseconds to delay. |

## Remarks

This function waits a specified number of milliseconds before returning. It
waits at least the specified time, but possibly longer due to OS
scheduling.

## Version

This function is available since SDL 2.0.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

