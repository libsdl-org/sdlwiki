# SDL_FALLTHROUGH

A macro to signal that a case statement without a `break` is intentional.

## Header File

Defined in [<SDL3/SDL_begin_code.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_begin_code.h)

## Syntax

```c
#define SDL_FALLTHROUGH [[fallthrough]]
```

## Remarks

C compilers have gotten more aggressive about warning when a switch's
`case` block does not end with a `break` or other flow control statement,
flowing into the next case's code, as this is a common accident that leads
to strange bugs. But sometimes falling through to the next case is the
correct and desired behavior. This symbol lets an app communicate this
intention to the compiler, so it doesn't generate a warning.

It is used like this:

```c
switch (x) {
    case 1:
        DoSomethingOnlyForOne();
        SDL_FALLTHROUGH;  // tell the compiler this was intentional.
    case 2:
        DoSomethingForOneAndTwo();
        break;
}
```

## Version

This macro is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryBeginCode](CategoryBeginCode)

