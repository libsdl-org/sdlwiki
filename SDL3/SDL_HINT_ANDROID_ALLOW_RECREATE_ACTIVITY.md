###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_ANDROID_ALLOW_RECREATE_ACTIVITY

A variable to control whether the SDL activity is allowed to be re-created.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_ANDROID_ALLOW_RECREATE_ACTIVITY "SDL_ANDROID_ALLOW_RECREATE_ACTIVITY"
```

## Remarks

If this hint is true, the activity can be recreated on demand by the OS,
and Java static data and C++ static data remain with their current values.
If this hint is false, then SDL will call exit() when you return from your
main function and the application will be terminated and then started fresh
each time.

The variable can be set to the following values:

- "0": The application starts fresh at each launch. (default)
- "1": The application activity can be recreated by the OS.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

