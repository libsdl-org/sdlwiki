# SDL_PathType

Types of filesystem entries.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
typedef enum SDL_PathType
{
    SDL_PATHTYPE_NONE,      /**< path does not exist */
    SDL_PATHTYPE_FILE,      /**< a normal file */
    SDL_PATHTYPE_DIRECTORY, /**< a directory */
    SDL_PATHTYPE_OTHER      /**< something completely different like a device node (not a symlink, those are always followed) */
} SDL_PathType;
```

## Remarks

Note that there may be other sorts of items on a filesystem: devices, named
pipes, etc. They are currently reported as
[SDL_PATHTYPE_OTHER](SDL_PATHTYPE_OTHER).

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_PathInfo](SDL_PathInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryFilesystem](CategoryFilesystem)

