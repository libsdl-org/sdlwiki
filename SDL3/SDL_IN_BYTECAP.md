###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_IN_BYTECAP

Macro that annotates function params with input buffer size.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_IN_BYTECAP(x) _In_bytecount_(x)
```

## Remarks

If we were to annotate `memcpy`:

```c
void *memcpy(void *dst, SDL_IN_BYTECAP(len) const void *src, size_t len);
```

This notes that `src` should be `len` bytes in size and is only read by the
function. The compiler or other analysis tools can warn when this doesn't
appear to be the case.

On compilers without this annotation mechanism, this is defined to nothing.

## Version

This macro is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

