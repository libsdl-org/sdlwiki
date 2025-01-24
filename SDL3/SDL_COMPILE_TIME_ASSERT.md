# SDL_COMPILE_TIME_ASSERT

A compile-time assertion.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_COMPILE_TIME_ASSERT(name, x) FailToCompileIf_x_IsFalse(x)
```

## Macro Parameters

|          |                                             |
| -------- | ------------------------------------------- |
| **name** | a unique identifier for this assertion.     |
| **x**    | the value to test. Must be a boolean value. |

## Remarks

This can check constant values _known to the compiler at build time_ for
correctness, and end the compile with the error if they fail.

Often times these are used to verify basic truths, like the size of a
datatype is what is expected:

```c
SDL_COMPILE_TIME_ASSERT(uint32_size, sizeof(Uint32) == 4);
```

The `name` parameter must be a valid C symbol, and must be unique across
all compile-time asserts in the same compilation unit (one run of the
compiler), or the build might fail with cryptic errors on some targets.
This is used with a C language trick that works on older compilers that
don't support better assertion techniques.

If you need an assertion that operates at runtime, on variable data, you
should try [SDL_assert](SDL_assert) instead.

## Thread Safety

This macro doesn't generate any code to run.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_assert](SDL_assert)






----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

