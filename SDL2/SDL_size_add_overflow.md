# SDL_size_add_overflow

If a + b would overflow, return -1.

## Header File

Defined in [SDL_stdinc.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_stdinc.h)

## Syntax

```c
SDL_FORCE_INLINE int SDL_size_add_overflow (size_t a, size_t b, size_t *ret);
```

## Remarks

Otherwise store a + b via ret and return 0.

## Version

This function is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdInc](CategoryStdInc)

