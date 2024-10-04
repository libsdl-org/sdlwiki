###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GlobDirectory

Enumerate a directory tree, filtered by pattern, and return a list.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
char ** SDL_GlobDirectory(const char *path, const char *pattern, SDL_GlobFlags flags, int *count);
```

## Function Parameters

|                                |             |                                                                                   |
| ------------------------------ | ----------- | --------------------------------------------------------------------------------- |
| const char *                   | **path**    | the path of the directory to enumerate.                                           |
| const char *                   | **pattern** | the pattern that files in the directory must match. Can be NULL.                  |
| [SDL_GlobFlags](SDL_GlobFlags) | **flags**   | `SDL_GLOB_*` bitflags that affect this search.                                    |
| int *                          | **count**   | on return, will be set to the number of items in the returned array. Can be NULL. |

## Return Value

(char **) Returns an array of strings on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This is a single
allocation that should be freed with [SDL_free](SDL_free)() when it is no
longer needed.

## Remarks

Files are filtered out if they don't match the string in `pattern`, which
may contain wildcard characters '*' (match everything) and '?' (match one
character). If pattern is NULL, no filtering is done and all results are
returned. Subdirectories are permitted, and are specified with a path
separator of '/'. Wildcard characters '*' and '?' never match a path
separator.

`flags` may be set to [SDL_GLOB_CASEINSENSITIVE](SDL_GLOB_CASEINSENSITIVE)
to make the pattern matching case-insensitive.

The returned array is always NULL-terminated, for your iterating
convenience, but if `count` is non-NULL, on return it will contain the
number of items in the array, not counting the NULL terminator.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

