# SDL_EnumerateDirectory

Enumerate a directory through a callback function.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
bool SDL_EnumerateDirectory(const char *path, SDL_EnumerateDirectoryCallback callback, void *userdata);
```

## Function Parameters

|                                                                  |              |                                                            |
| ---------------------------------------------------------------- | ------------ | ---------------------------------------------------------- |
| const char *                                                     | **path**     | the path of the directory to enumerate.                    |
| [SDL_EnumerateDirectoryCallback](SDL_EnumerateDirectoryCallback) | **callback** | a function that is called for each entry in the directory. |
| void *                                                           | **userdata** | a pointer that is passed to `callback`.                    |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function provides every directory entry through an app-provided
callback, called once for each directory entry, until all results have been
provided or the callback returns either
[SDL_ENUM_SUCCESS](SDL_ENUM_SUCCESS) or
[SDL_ENUM_FAILURE](SDL_ENUM_FAILURE).

This will return false if there was a system problem in general, or if a
callback returns [SDL_ENUM_FAILURE](SDL_ENUM_FAILURE). A successful return
means a callback returned [SDL_ENUM_SUCCESS](SDL_ENUM_SUCCESS) to halt
enumeration, or all directory entries were enumerated.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

