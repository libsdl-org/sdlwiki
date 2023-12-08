###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetVersion

Get the version of SDL that is linked against your program.

## Syntax

```c
void SDL_GetVersion(SDL_version * ver);

```

## Function Parameters

|             |                                                                                |
| ----------- | ------------------------------------------------------------------------------ |
| **ver**     | the [SDL_version](SDL_version.md) structure that contains the version information |

## Remarks

If you are linking to SDL dynamically, then it is possible that the current
version will be different than the version you compiled against. This
function returns the current version, while [SDL_VERSION](SDL_VERSION.md)() is
a macro that tells you what version you compiled with.

This function may be called safely at any time, even before
[SDL_Init](SDL_Init.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetRevision](SDL_GetRevision.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVersion](CategoryVersion.md)
