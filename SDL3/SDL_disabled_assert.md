###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_disabled_assert

The macro used when an assertion is disabled.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_disabled_assert(condition) \
    do { (void) sizeof ((condition)); } while (SDL_NULL_WHILE_LOOP_CONDITION)
```

## Macro Parameters

|               |                                                      |
| ------------- | ---------------------------------------------------- |
| **condition** | the condition to assert (but not actually run here). |

## Remarks

This isn't for direct use by apps, but this is the code that is inserted
when an [SDL_assert](SDL_assert) is disabled (perhaps in a release build).

The code does nothing, but wraps `condition` in a sizeof operator, which
generates no code and has no side effects, but avoid compiler warnings
about unused variables.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAssert](CategoryAssert)

