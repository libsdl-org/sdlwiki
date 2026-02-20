# SDL_GetPathInfo

Get information about a filesystem path.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
bool SDL_GetPathInfo(const char *path, SDL_PathInfo *info);
```

## Function Parameters

|                                |          |                                                                                                    |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------------------- |
| const char *                   | **path** | the path to query.                                                                                 |
| [SDL_PathInfo](SDL_PathInfo) * | **info** | a pointer filled in with information about the path, or NULL to check for the existence of a file. |

## Return Value

(bool) Returns true on success or false if the file doesn't exist, or
another failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Symlinks, on filesystems that support them, are always followed, so you
will always get information on what the symlink eventually points to, and
not the symlink itself.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

