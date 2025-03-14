# SDL_GetVersion

Get the version of SDL that is linked against your program.

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_version.h)

## Syntax

```c
void SDL_GetVersion(SDL_version * ver);
```

## Function Parameters

|                              |         |                                                                                 |
| ---------------------------- | ------- | ------------------------------------------------------------------------------- |
| [SDL_version](SDL_version) * | **ver** | the [SDL_version](SDL_version) structure that contains the version information. |

## Remarks

If you are linking to SDL dynamically, then it is possible that the current
version will be different than the version you compiled against. This
function returns the current version, while [SDL_VERSION](SDL_VERSION)() is
a macro that tells you what version you compiled with.

This function may be called safely at any time, even before
[SDL_Init](SDL_Init)().

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetRevision](SDL_GetRevision)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVersion](CategoryVersion)

