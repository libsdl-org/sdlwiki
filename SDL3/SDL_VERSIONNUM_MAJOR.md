# SDL_VERSIONNUM_MAJOR

This macro extracts the major version from a version number

## Header File

Defined in [<SDL3/SDL_version.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h)

## Syntax

```c
#define SDL_VERSIONNUM_MAJOR(version) ((version) / 1000000)
```

## Macro Parameters

|             |                     |
| ----------- | ------------------- |
| **version** | the version number. |

## Remarks

1002003 becomes 1.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)

