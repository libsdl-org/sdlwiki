###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_version

Information about the version of SDL in use.

## Header File

Defined in [SDL_version.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_version.h)

## Syntax

```c
typedef struct SDL_version
{
    Uint8 major;        /**< major version */
    Uint8 minor;        /**< minor version */
    Uint8 patch;        /**< update version */
} SDL_version;
```

## Remarks

Represents the library's version as three levels: major revision
(increments with massive changes, additions, and enhancements), minor
revision (increments with backwards-compatible changes to the major
revision), and patchlevel (increments with fixes to the minor revision).

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

- [SDL_VERSION](SDL_VERSION)
- [SDL_GetVersion](SDL_GetVersion)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryVersion](CategoryVersion)


