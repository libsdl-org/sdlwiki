###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SwapLE64

Swap a 64-bit value from littleendian to native format.

## Header File

Defined in [SDL_endian.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_endian.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_SwapLE64(X) SwapOnlyIfNecessary(X)
```

## Macro Parameters

|           |                    |
| --------- | ------------------ |
| **X**     | the value to swap. |

## Return Value

Returns the byte-swapped value.

## Remarks

If this is running on a littleendian system, `X` is returned unchanged.

This macro never references `X` more than once, avoiding side effects.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

