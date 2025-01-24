# SDL_zerop

Clear an object's memory to zero, using a pointer.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_zerop(x) SDL_memset((x), 0, sizeof(*(x)))
```

## Macro Parameters

|       |                                   |
| ----- | --------------------------------- |
| **x** | a pointer to the object to clear. |

## Remarks

This is wrapper over [SDL_memset](SDL_memset) that handles calculating the
object size, so there's no chance of copy/paste errors, and the code is
cleaner.

This requires a pointer to an object, not an object itself, nor an array.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_zero](SDL_zero)
- [SDL_zeroa](SDL_zeroa)






----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

