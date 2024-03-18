###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPathInfo

Get information about a filesystem path.

## Syntax

```c
int SDL_GetPathInfo(const char *path, SDL_PathInfo *info);

```

## Function Parameters

|              |                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------- |
| **path**     | the path to query                                                                                 |
| **info**     | a pointer filled in with information about the path, or NULL to check for the existence of a file |

## Return Value

Returns 0 on success or a negative error code if the file doesn't exist, or
another failure; call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

