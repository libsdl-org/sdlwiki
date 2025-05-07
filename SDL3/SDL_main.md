# SDL_main

An app-supplied function for program entry.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
int SDL_main(int argc, char *argv[]);
```

## Function Parameters

|         |          |                                       |
| ------- | -------- | ------------------------------------- |
| int     | **argc** | an ANSI-C style main function's argc. |
| char ** | **argv** | an ANSI-C style main function's argv. |

## Return Value

(int) Returns an ANSI-C main return code; generally 0 is considered
successful program completion, and small non-zero values are considered
errors.

## Remarks

Apps do not directly create this function; they should create a standard
ANSI-C `main` function instead. If SDL needs to insert some startup code
before `main` runs, or the platform doesn't actually _use_ a function
called "main", SDL will do some macro magic to redefine `main` to
[`SDL_main`](SDL_main) and provide its own `main`.

Apps should include `SDL_main.h` in the same file as their `main` function,
and they should not use that symbol for anything else in that file, as it
might get redefined.

This function is only provided by the app if it isn't using
[SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS).

Program startup is a surprisingly complex topic. Please see
[README-main-functions](README-main-functions), (or
docs/README-main-functions.md in the source tree) for a more detailed
explanation.

## Thread Safety

This is the program entry point.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

