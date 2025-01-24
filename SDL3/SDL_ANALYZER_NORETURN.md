# SDL_ANALYZER_NORETURN

A macro to tag a function as never-returning (for analysis purposes).

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_ANALYZER_NORETURN __attribute__((analyzer_noreturn))
```

## Remarks

This is almost identical to [SDL_NORETURN](SDL_NORETURN), except functions
marked with this _can_ actually return. The difference is that this isn't
used for code generation, but rather static analyzers use this information
to assume truths about program state and available code paths.
Specifically, this tag is useful for writing an assertion mechanism.
Indeed, [SDL_assert](SDL_assert) uses this tag behind the scenes.
Generally, apps that don't understand the specific use-case for this tag
should avoid using it directly.

On compilers without analyzer_noreturn support, this is defined to nothing.

This symbol is used in SDL's headers, but apps and other libraries are
welcome to use it for their own interfaces as well.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

