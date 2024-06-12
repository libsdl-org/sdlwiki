###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetVersion

Get the version of SDL that is linked against your program.

## Header File

Defined in [<SDL3/SDL_version.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h)

## Syntax

```c
int SDL_GetVersion(void);
```

## Return Value

(int) Returns the version of the linked library.

## Remarks

If you are linking to SDL dynamically, then it is possible that the current
version will be different than the version you compiled against. This
function returns the current version, while [SDL_VERSION](SDL_VERSION) is
the version you compiled with.

This function may be called safely at any time, even before
[SDL_Init](SDL_Init)().

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
const int compiled = SDL_VERSION;  /* hardcoded number from SDL headers */
const int linked = SDL_GetVersion();  /* reported by linked SDL library */

SDL_Log("We compiled against SDL version %d.%d.%d ...\n",
        SDL_VERSIONNUM_MAJOR(compiled),
        SDL_VERSIONNUM_MINOR(compiled),
        SDL_VERSIONNUM_MICRO(compiled));

SDL_Log("But we are linking against SDL version %d.%d.%d.\n",
        SDL_VERSIONNUM_MAJOR(linked),
        SDL_VERSIONNUM_MINOR(linked),
        SDL_VERSIONNUM_MICRO(linked));
```

## See Also

- [SDL_GetRevision](SDL_GetRevision)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVersion](CategoryVersion)

