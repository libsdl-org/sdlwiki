# SDL_VERSIONNUM_MICRO

This macro extracts the micro version from a version number

## Header File

Defined in [<SDL3/SDL_version.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h)

## Syntax

```c
#define SDL_VERSIONNUM_MICRO(version) ((version) % 1000)
```

## Macro Parameters

|             |                     |
| ----------- | ------------------- |
| **version** | the version number. |

## Remarks

1002003 becomes 3.

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)

