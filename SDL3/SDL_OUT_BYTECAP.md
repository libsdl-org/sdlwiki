# SDL_OUT_BYTECAP

Macro that annotates function params with output buffer size.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_OUT_BYTECAP(x) _Out_bytecap_(x)
```

## Remarks

If we were to annotate `memcpy`:

```c
void *memcpy(SDL_OUT_BYTECAP(bufsize) void *dst, const void *src, size_t bufsize);
```

This notes that `dst` should have a capacity of `bufsize` bytes in size,
and is only written to by the function. The compiler or other analysis
tools can warn when this doesn't appear to be the case.

On compilers without this annotation mechanism, this is defined to nothing.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

