# SDL_RenamePath

Rename a file or directory.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
bool SDL_RenamePath(const char *oldpath, const char *newpath);
```

## Function Parameters

|              |             |               |
| ------------ | ----------- | ------------- |
| const char * | **oldpath** | the old path. |
| const char * | **newpath** | the new path. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If the file at `newpath` already exists, it will replaced.

Note that this will not copy files across filesystems/drives/volumes, as
that is a much more complicated (and possibly time-consuming) operation.

Which is to say, if this function fails, [SDL_CopyFile](SDL_CopyFile)() to
a temporary file in the same directory as `newpath`, then
[SDL_RenamePath](SDL_RenamePath)() from the temporary file to `newpath` and
[SDL_RemovePath](SDL_RemovePath)() on `oldpath` might work for files.
Renaming a non-empty directory across filesystems is dramatically more
complex, however.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

