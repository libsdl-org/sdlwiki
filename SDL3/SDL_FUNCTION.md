# SDL_FUNCTION

A macro that reports the current function being compiled.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_FUNCTION __FUNCTION__
```

## Remarks

If SDL can't figure how the compiler reports this, it will use "???".

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAssert](CategoryAssert)

