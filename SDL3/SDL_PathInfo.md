# SDL_PathInfo

Information about a path on the filesystem.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
typedef struct SDL_PathInfo
{
    SDL_PathType type;      /**< the path type */
    Uint64 size;            /**< the file size in bytes */
    SDL_Time create_time;   /**< the time when the path was created */
    SDL_Time modify_time;   /**< the last time the path was modified */
    SDL_Time access_time;   /**< the last time the path was read */
} SDL_PathInfo;
```

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_GetPathInfo](SDL_GetPathInfo)
- [SDL_GetStoragePathInfo](SDL_GetStoragePathInfo)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryFilesystem](CategoryFilesystem)

