# SDL_InvalidParamError

A macro to standardize error reporting on unsupported operations.

## Header File

Defined in [<SDL3/SDL_error.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h)

## Syntax

```c
#define SDL_InvalidParamError(param)    SDL_SetError("Parameter '%s' is invalid", (param))
```

## Remarks

This simply calls [SDL_SetError](SDL_SetError)() with a standardized error
string, for convenience, consistency, and clarity.

A common usage pattern inside SDL is this:

```c
bool MyFunction(const char *str) {
    if (!str) {
        return SDL_InvalidParamError("str");  // returns false.
    }
    DoSomething(str);
    return true;
}
```

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryError](CategoryError)

