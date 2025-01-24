# SDL_max

Return the greater of two values.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_max(x, y) (((x) > (y)) ? (x) : (y))
```

## Macro Parameters

|       |                              |
| ----- | ---------------------------- |
| **x** | the first value to compare.  |
| **y** | the second value to compare. |

## Return Value

Returns the lesser of `x` and `y`.

## Remarks

This is a helper macro that might be more clear than writing out the
comparisons directly, and works with any type that can be compared with the
`>` operator. However, it double-evaluates both its parameters, so do not
use expressions with side-effects here.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

