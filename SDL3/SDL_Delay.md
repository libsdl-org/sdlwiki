# SDL_Delay

Wait a specified number of milliseconds before returning.

## Header File

Defined in [<SDL3/SDL_timer.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

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

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_DelayNS](SDL_DelayNS)
- [SDL_DelayPrecise](SDL_DelayPrecise)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

