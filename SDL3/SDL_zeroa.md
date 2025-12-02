# SDL_zeroa

Clear an array's memory to zero.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_zeroa(x) SDL_memset((x), 0, sizeof((x)))
```

## Macro Parameters

|       |                    |
| ----- | ------------------ |
| **x** | an array to clear. |

## Remarks

This is wrapper over [SDL_memset](SDL_memset) that handles calculating the
array size, so there's no chance of copy/paste errors, and the code is
cleaner.

This requires an array, not an object, nor a pointer to an object.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_zero](SDL_zero)
- [SDL_zerop](SDL_zerop)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

