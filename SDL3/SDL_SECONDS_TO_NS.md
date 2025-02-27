# SDL_SECONDS_TO_NS

Convert seconds to nanoseconds.

## Header File

Defined in [<SDL3/SDL_timer.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

## Syntax

```c
#define SDL_SECONDS_TO_NS(S)    (((Uint64)(S)) * SDL_NS_PER_SECOND)
```

## Macro Parameters

|       |                                   |
| ----- | --------------------------------- |
| **S** | the number of seconds to convert. |

## Return Value

Returns S, expressed in nanoseconds.

## Remarks

This only converts whole numbers, not fractional seconds.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryTimer](CategoryTimer)

