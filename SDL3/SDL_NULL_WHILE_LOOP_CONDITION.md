# SDL_NULL_WHILE_LOOP_CONDITION

A macro for wrapping code in `do {} while (0);` without compiler warnings.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_NULL_WHILE_LOOP_CONDITION (0)
```

## Remarks

Visual Studio with really aggressive warnings enabled needs this to avoid
compiler complaints.

the `do {} while (0);` trick is useful for wrapping code in a macro that
may or may not be a single statement, to avoid various C language
accidents.

To use:

```c
do { SomethingOnce(); } while (SDL_NULL_WHILE_LOOP_CONDITION (0));
```

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAssert](CategoryAssert)

