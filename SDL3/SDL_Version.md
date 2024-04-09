###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Version

Information about the version of SDL in use.

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_version.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef struct SDL_Version
{
    Uint8 major;        /**< major version */
    Uint8 minor;        /**< minor version */
    Uint8 patch;        /**< update version */
} SDL_Version;
```

## Remarks

Represents the library's version as three levels: major revision
(increments with massive changes, additions, and enhancements), minor
revision (increments with backwards-compatible changes to the major
revision), and patchlevel (increments with fixes to the minor revision).

## Version

This struct is available since SDL 3.0.0.

## See Also

* [SDL_VERSION](SDL_VERSION)
* [SDL_GetVersion](SDL_GetVersion)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

