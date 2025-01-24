# SDL_PRINTF_FORMAT_STRING

Macro that annotates function params as printf-style format strings.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_PRINTF_FORMAT_STRING _Printf_format_string_
```

## Remarks

If we were to annotate `fprintf`:

```c
int fprintf(FILE *f, SDL_PRINTF_FORMAT_STRING const char *fmt, ...);
```

This notes that `fmt` should be a printf-style format string. The compiler
or other analysis tools can warn when this doesn't appear to be the case.

On compilers without this annotation mechanism, this is defined to nothing.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

