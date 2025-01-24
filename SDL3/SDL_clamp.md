# SDL_clamp

Return a value clamped to a range.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_clamp(x, a, b) (((x) < (a)) ? (a) : (((x) > (b)) ? (b) : (x)))
```

## Macro Parameters

|       |                       |
| ----- | --------------------- |
| **x** | the value to compare. |
| **a** | the low end value.    |
| **b** | the high end value.   |

## Return Value

Returns x, clamped between a and b.

## Remarks

If `x` is outside the range a values between `a` and `b`, the returned
value will be `a` or `b` as appropriate. Otherwise, `x` is returned.

This macro will produce incorrect results if `b` is less than `a`.

This is a helper macro that might be more clear than writing out the
comparisons directly, and works with any type that can be compared with the
`<` and `>` operators. However, it double-evaluates all its parameters, so
do not use expressions with side-effects here.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

