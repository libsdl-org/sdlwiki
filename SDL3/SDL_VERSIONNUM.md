###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_VERSIONNUM

This macro turns the version numbers into a numeric value.

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_VERSIONNUM(major, minor, patch) \
    ((major) << 24 | (minor) << 8 | (patch) << 0)
```

## Macro Parameters

|               |                           |
| ------------- | ------------------------- |
| **major**     | the major version number. |
| **minor**     | the minorversion number.  |
| **patch**     | the patch version number. |

## Remarks

(1,2,3) becomes 0x1000203.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

