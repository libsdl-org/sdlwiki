###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AndroidRequestPermission

Request permissions at runtime.

## Syntax

```c
SDL_bool SDL_AndroidRequestPermission(const char *permission);

```

## Function Parameters

|                    |                            |
| ------------------ | -------------------------- |
| **permission**     | The permission to request. |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the permission was granted,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

This blocks the calling thread until the permission is granted or denied.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
