# SDL_NS_TO_US

Convert nanoseconds to microseconds.

## Header File

Defined in [<SDL3/SDL_timer.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

## Syntax

```c
#define SDL_NS_TO_US(NS)        ((NS) / SDL_NS_PER_US)
```

## Macro Parameters

|        |                                       |
| ------ | ------------------------------------- |
| **NS** | the number of nanoseconds to convert. |

## Return Value

Returns NS, expressed in microseconds.

## Remarks

This performs a division, so the results can be dramatically different if
`NS` is an integer or floating point value.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryTimer](CategoryTimer)

