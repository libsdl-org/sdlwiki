###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CopyFile

Copy a file.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
bool SDL_CopyFile(const char *oldpath, const char *newpath);
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

If the file at `newpath` already exists, it will be overwritten with the
contents of the file at `oldpath`.

This function will block until the copy is complete, which might be a
significant time for large files on slow disks. On some platforms, the copy
can be handed off to the OS itself, but on others SDL might just open both
paths, and read from one and write to the other.

Note that this is not an atomic operation! If something tries to read from
`newpath` while the copy is in progress, it will see an incomplete copy of
the data, and if the calling thread terminates (or the power goes out)
during the copy, `oldpath`'s previous contents will be gone, replaced with
an incomplete copy of the data. To avoid this risk, it is recommended that
the app copy to a temporary file in the same directory as `newpath`, and if
the copy is successful, use [SDL_RenamePath](SDL_RenamePath)() to replace
`newpath` with the temporary file. This will ensure that reads of `newpath`
will either see a complete copy of the data, or it will see the pre-copy
state of `newpath`.

This function attempts to synchronize the newly-copied data to disk before
returning, if the platform allows it, so that the renaming trick will not
have a problem in a system crash or power failure, where the file could be
renamed but the contents never made it from the system file cache to the
physical disk.

If the copy fails for any reason, the state of `newpath` is undefined. It
might be half a copy, it might be the untouched data of what was already
there, or it might be a zero-byte file, etc.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

