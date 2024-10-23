###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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
provided or the callback returns <= 0.

This will return false if there was a system problem in general, or if a
callback returns -1. A successful return means a callback returned 1 to
halt enumeration, or all directory entries were enumerated.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

