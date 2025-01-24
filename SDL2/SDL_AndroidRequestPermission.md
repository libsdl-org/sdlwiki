# SDL_AndroidRequestPermission

Request permissions at runtime.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
SDL_bool SDL_AndroidRequestPermission(const char *permission);
```

## Function Parameters

|              |                |                            |
| ------------ | -------------- | -------------------------- |
| const char * | **permission** | The permission to request. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the permission was
granted, [SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This blocks the calling thread until the permission is granted or denied.

## Version

This function is available since SDL 2.0.14.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

