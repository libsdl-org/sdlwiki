# SDL_PRINTF_VARARG_FUNC

Macro that annotates a vararg function that operates like printf.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRINTF_VARARG_FUNC( fmtargnumber ) __attribute__ (( format( __printf__, fmtargnumber, fmtargnumber+1 )))
```

## Remarks

If we were to annotate `fprintf`:

```c
int fprintf(FILE *f, const char *fmt, ...) SDL_PRINTF_VARARG_FUNC(2);
```

This notes that the second parameter should be a printf-style format
string, followed by `...`. The compiler or other analysis tools can warn
when this doesn't appear to be the case.

On compilers without this annotation mechanism, this is defined to nothing.

This can (and should) be used with
[SDL_PRINTF_FORMAT_STRING](SDL_PRINTF_FORMAT_STRING) as well, which between
them will cover at least Visual Studio, GCC, and Clang.

## Version

This macro is available since SDL 3.2.0.

## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

