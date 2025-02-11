# SDL_VERSIONNUM

This macro turns the version numbers into a numeric value.

## Header File

Defined in [<SDL3/SDL_version.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h)

## Syntax

```c
#define SDL_VERSIONNUM(major, minor, patch) \
    ((major) * 1000000 + (minor) * 1000 + (patch))
```

## Macro Parameters

|           |                           |
| --------- | ------------------------- |
| **major** | the major version number. |
| **minor** | the minorversion number.  |
| **patch** | the patch version number. |

## Remarks

(1,2,3) becomes 1002003.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)

