###### (This function is part of SDL_rtf, a separate library from SDL.)
# SDL_RTF_VERSION_ATLEAST

This macro will evaluate to true if compiled with SDL_rtf at least X.Y.Z.

## Header File

Defined in [<SDL3_rtf/SDL_rtf.h>](https://github.com/libsdl-org/SDL_rtf/blob/main/include/SDL3_rtf/SDL_rtf.h)

## Syntax

```c
#define SDL_RTF_VERSION_ATLEAST(X, Y, Z) \
    ((SDL_RTF_MAJOR_VERSION >= X) && \
     (SDL_RTF_MAJOR_VERSION > X || SDL_RTF_MINOR_VERSION >= Y) && \
     (SDL_RTF_MAJOR_VERSION > X || SDL_RTF_MINOR_VERSION > Y || SDL_RTF_MICRO_VERSION >= Z))
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

