###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

Returns [SDL_TRUE](SDL_TRUE) if the permission was granted,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This blocks the calling thread until the permission is granted or denied.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAndroid](CategoryAndroid)


