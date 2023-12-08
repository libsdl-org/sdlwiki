###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
