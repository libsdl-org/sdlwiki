###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_assert_always

An assertion test that is always performed.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_assert_always(condition) SDL_enabled_assert(condition)
```

## Macro Parameters

|               |                        |
| ------------- | ---------------------- |
| **condition** | boolean value to test. |

## Remarks

This macro is always enabled no matter what
[SDL_ASSERT_LEVEL](SDL_ASSERT_LEVEL) is set to. You almost never want to
use this, as it could trigger on an end-user's system, crashing your
program.

One can set the environment variable "[SDL_ASSERT](SDL_ASSERT)" to one of
several strings ("abort", "break", "retry", "ignore", "always_ignore") to
force a default behavior, which may be desirable for automation purposes.
If your platform requires GUI interfaces to happen on the main thread but
you're debugging an assertion in a background thread, it might be desirable
to set this to "break" so that your debugger takes control as soon as
assert is triggered, instead of risking a bad UI interaction (deadlock,
etc) in the application.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAssert](CategoryAssert)

