###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_VERSION

Macro to determine SDL version program was compiled against.

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_version.h)

## Syntax

```c
#define SDL_VERSION(x)                          \
{                                   \
    (x)->major = SDL_MAJOR_VERSION;                 \
    (x)->minor = SDL_MINOR_VERSION;                 \
    (x)->patch = SDL_PATCHLEVEL;                    \
}
```

## Macro Parameters

|           |                                                                 |
| --------- | --------------------------------------------------------------- |
| **x**     | A pointer to a [SDL_version](SDL_version) struct to initialize. |

## Remarks

This macro fills in a [SDL_version](SDL_version) structure with the version
of the library you compiled against. This is determined by what header the
compiler uses. Note that if you dynamically linked the library, you might
have a slightly newer or older version at runtime. That version can be
determined with [SDL_GetVersion](SDL_GetVersion)(), which, unlike
[SDL_VERSION](SDL_VERSION)(), is not a macro.

## Code Examples

```c
SDL_version compiled;
SDL_version linked;

SDL_VERSION(&compiled);
SDL_GetVersion(&linked);
SDL_Log("We compiled against SDL version %u.%u.%u ...\n",
       compiled.major, compiled.minor, compiled.patch);
SDL_Log("But we are linking against SDL version %u.%u.%u.\n",
       linked.major, linked.minor, linked.patch);
```

## See Also

* [SDL_version](SDL_version)
* [SDL_GetVersion](SDL_GetVersion)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryVersion](CategoryVersion)


