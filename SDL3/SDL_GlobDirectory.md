###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GlobDirectory

Enumerate a directory tree, filtered by pattern, and return a list.

## Header File

Defined in [SDL_filesystem.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
extern DECLSPEC char **SDLCALL SDL_GlobDirectory(const char *path, const char *pattern, Uint32 flags, int *count);

```

## Function Parameters

|                 |                                                                                   |
| --------------- | --------------------------------------------------------------------------------- |
| **path**        | the path of the directory to enumerate                                            |
| **pattern**     | the pattern that files in the directory must match. Can be NULL.                  |
| **flags**       | `SDL_GLOB_*` bitflags that affect this search.                                    |
| **count**       | on return, will be set to the number of items in the returned array. Can be NULL. |

## Return Value

Returns an array of strings on success or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. The caller should pass
the returned pointer to [SDL_free](SDL_free) when done with it.

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

You must free the returned pointer with [SDL_free](SDL_free)() when done
with it.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

