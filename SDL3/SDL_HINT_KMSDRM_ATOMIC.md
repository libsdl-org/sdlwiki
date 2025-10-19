# SDL_HINT_KMSDRM_ATOMIC

A variable that controls whether KMSDRM will use "atomic" functionality.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_KMSDRM_ATOMIC "SDL_KMSDRM_ATOMIC"
```

## Remarks

The KMSDRM backend can use atomic commits, if both DRM_CLIENT_CAP_ATOMIC
and DRM_CLIENT_CAP_UNIVERSAL_PLANES is supported by the system. As of SDL
3.4.0, it will favor this functionality, but in case this doesn't work well
on a given system or other surprises, this hint can be used to disable it.

This hint can not enable the functionality if it isn't available.

The variable can be set to the following values:

- "0": SDL will not use the KMSDRM "atomic" functionality.
- "1": SDL will allow usage of the KMSDRM "atomic" functionality. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

