# SDL_CreateDirectory

Create a directory, and any missing parent directories.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
bool SDL_CreateDirectory(const char *path);
```

## Function Parameters

|              |          |                                      |
| ------------ | -------- | ------------------------------------ |
| const char * | **path** | the path of the directory to create. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This reports success if `path` already exists as a directory.

If parent directories are missing, it will also create them. Note that if
this fails, it will not remove any parent directories it already made.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryFilesystem](CategoryFilesystem)

