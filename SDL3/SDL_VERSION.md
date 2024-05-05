###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_VERSION

Macro to determine SDL version program was compiled against.

## Header File

Defined in [<SDL3/SDL_version.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h)

## Syntax

```c
#define SDL_VERSION(x)                \
{                                     \
    (x)->major = SDL_MAJOR_VERSION;   \
    (x)->minor = SDL_MINOR_VERSION;   \
    (x)->patch = SDL_PATCHLEVEL;      \
}
```

## Macro Parameters

|           |                                                                  |
| --------- | ---------------------------------------------------------------- |
| **x**     | A pointer to an [SDL_Version](SDL_Version) struct to initialize. |

## Remarks

This macro fills in an [SDL_Version](SDL_Version) structure with the
version of the library you compiled against. This is determined by what
header the compiler uses. Note that if you dynamically linked the library,
you might have a slightly newer or older version at runtime. That version
can be determined with [SDL_GetVersion](SDL_GetVersion)(), which, unlike
[SDL_VERSION](SDL_VERSION)(), is not a macro.

## Version

This macro is available since SDL 3.0.0.

## See Also

- [SDL_Version](SDL_Version)
- [SDL_GetVersion](SDL_GetVersion)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

