###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_US_TO_NS

Convert microseconds to nanoseconds.

## Header File

Defined in [<SDL3/SDL_timer.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

## Syntax

```c
#define SDL_US_TO_NS(US)        (((Uint64)(US)) * SDL_NS_PER_US)
```

## Macro Parameters

|        |                                        |
| ------ | -------------------------------------- |
| **US** | the number of microseconds to convert. |

## Return Value

Return US, expressed in nanoseconds.

## Remarks

This only converts whole numbers, not fractional microseconds.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryTimer](CategoryTimer)

