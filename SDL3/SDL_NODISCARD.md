# SDL_NODISCARD

A macro to tag a function's return value as critical.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_NODISCARD [[nodiscard]]
```

## Remarks

This is a hint to the compiler that a function's return value should not be
ignored.

If an NODISCARD function's return value is thrown away (the function is
called as if it returns `void`), the compiler will issue a warning.

While it's generally good practice to check return values for errors, often
times legitimate programs do not for good reasons. Be careful about what
functions are tagged as NODISCARD. It operates best when used on a function
that's failure is surprising and catastrophic; a good example would be a
program that checks the return values of all its file write function calls
but not the call to close the file, which it assumes incorrectly never
fails.

Function callers that want to throw away a NODISCARD return value can call
the function with a `(void)` cast, which informs the compiler the act is
intentional.

On compilers without nodiscard support, this is defined to nothing.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

