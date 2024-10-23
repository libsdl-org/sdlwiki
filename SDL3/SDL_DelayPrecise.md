###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_DelayPrecise

Wait a specified number of nanoseconds before returning.

## Header File

Defined in [<SDL3/SDL_timer.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

## Syntax

```c
void SDL_DelayPrecise(Uint64 ns);
```

## Function Parameters

|        |        |                                     |
| ------ | ------ | ----------------------------------- |
| Uint64 | **ns** | the number of nanoseconds to delay. |

## Remarks

This function waits a specified number of nanoseconds before returning. It
will attempt to wait as close to the requested time as possible, busy
waiting if necessary, but could return later due to OS scheduling.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

