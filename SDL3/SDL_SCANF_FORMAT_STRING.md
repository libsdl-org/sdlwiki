# SDL_SCANF_FORMAT_STRING

Macro that annotates function params as scanf-style format strings.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_SCANF_FORMAT_STRING _Scanf_format_string_impl_
```

## Remarks

If we were to annotate `fscanf`:

```c
int fscanf(FILE *f, SDL_SCANF_FORMAT_STRING const char *fmt, ...);
```

This notes that `fmt` should be a scanf-style format string. The compiler
or other analysis tools can warn when this doesn't appear to be the case.

On compilers without this annotation mechanism, this is defined to nothing.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

