# SDL_OUT_Z_CAP

Macro that annotates function params with output string buffer size.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_OUT_Z_CAP(x) _Out_z_cap_(x)
```

## Remarks

If we were to annotate `snprintf`:

```c
int snprintf(SDL_OUT_Z_CAP(maxlen) char *text, size_t maxlen, const char *fmt, ...);
```

This notes that `text` is a null-terminated C string, should be `maxlen`
bytes in size, and is only written to by the function. The compiler or
other analysis tools can warn when this doesn't appear to be the case.

On compilers without this annotation mechanism, this is defined to nothing.

## Version

This macro is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

