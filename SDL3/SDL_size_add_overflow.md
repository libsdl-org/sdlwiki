###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_size_add_overflow

If a + b would overflow, return -1.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_FORCE_INLINE int SDL_size_add_overflow (size_t a, size_t b, size_t *ret);
```

## Remarks

Otherwise store a + b via ret and return 0.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

