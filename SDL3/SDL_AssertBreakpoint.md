# SDL_AssertBreakpoint

The macro used when an assertion triggers a breakpoint.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_AssertBreakpoint() SDL_TriggerBreakpoint()
```

## Remarks

This isn't for direct use by apps; use [SDL_assert](SDL_assert) or
[SDL_TriggerBreakpoint](SDL_TriggerBreakpoint) instead.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAssert](CategoryAssert)

