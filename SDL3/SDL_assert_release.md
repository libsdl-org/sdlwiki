###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_assert_release

An assertion test that is performed even in release builds.

## Header File

Defined in [SDL_assert.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_assert_release(condition) SDL_disabled_assert(condition)
```

## Macro Parameters

|                   |                       |
| ----------------- | --------------------- |
| **condition**     | boolean value to test |

## Remarks

This macro is enabled when the [SDL_ASSERT_LEVEL](SDL_ASSERT_LEVEL) is >=
1, otherwise it is disabled. This is meant to be for tests that are cheap
to make and extremely unlikely to fail; generally it is frowned upon to
have an assertion failure in a release build, so these assertions generally
need to be of more than life-and-death importance if there's a chance they
might trigger. You should almost always consider handling these cases more
gracefully than an assert allows.

When assertions are disabled, this wraps `condition` in a `sizeof`
operator, which means any function calls and side effects will not run, but
the compiler will not complain about any otherwise-unused variables that
are only referenced in the assertion.

One can set the environment variable "[SDL_ASSERT](SDL_ASSERT)" to one of
several strings ("abort", "break", "retry", "ignore", "always_ignore") to
force a default behavior, which may be desirable for automation purposes.
If your platform requires GUI interfaces to happen on the main thread but
you're debugging an assertion in a background thread, it might be desirable
to set this to "break" so that your debugger takes control as soon as
assert is triggered, instead of risking a bad UI interaction (deadlock,
etc) in the application.

Note that [SDL_ASSERT](SDL_ASSERT) is an _environment variable_ and not an
SDL hint! Please refer to your platform's documentation for how to set it!

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

