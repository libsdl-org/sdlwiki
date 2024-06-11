###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_main

An app-supplied function for program entry.

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
int SDL_main(int argc, char *argv[]);
```

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
[README/main-functions](README/main-functions), (or
docs/README-main-functions.md in the source tree) for a more detailed
explanation.

## Thread Safety

This is the program entry point.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

