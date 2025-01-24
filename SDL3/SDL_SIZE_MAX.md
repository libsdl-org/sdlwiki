# SDL_SIZE_MAX

The largest value that a `size_t` can hold for the target platform.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_SIZE_MAX SIZE_MAX
```

## Remarks

`size_t` is generally the same size as a pointer in modern times, but this
can get weird on very old and very esoteric machines. For example, on a
16-bit Intel 286, you might have a 32-bit "far" pointer (16-bit segment
plus 16-bit offset), but `size_t` is 16 bits, because it can only deal with
the offset into an individual segment.

In modern times, it's generally expected to cover an entire linear address
space. But be careful!

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

