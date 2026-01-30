# SDL_HINT_OPENXR_LIBRARY

A variable that specifies the library name to use when loading the OpenXR loader.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_OPENXR_LIBRARY "SDL_OPENXR_LIBRARY"
```

## Remarks

By default, SDL will try the system default name, but on some platforms
like Windows, debug builds of the OpenXR loader have a different name, and
are not always directly compatible with release applications. Setting this
hint allows you to compensate for this difference in your app when
applicable.

This hint should be set before the OpenXR loader is loaded. For example,
creating an OpenXR GPU device will load the OpenXR loader.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

