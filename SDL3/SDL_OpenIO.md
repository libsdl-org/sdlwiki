###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OpenIO

Create a custom [SDL_IOStream](SDL_IOStream).

## Syntax

```c
SDL_IOStream* SDL_OpenIO(const SDL_IOStreamInterface *iface, void *userdata);

```

## Function Parameters

|                  |                                                                             |
| ---------------- | --------------------------------------------------------------------------- |
| **iface**        | The function pointers that implement this [SDL_IOStream](SDL_IOStream).     |
| **userdata**     | The app-controlled pointer that is passed to iface's functions when called. |

## Return Value

Returns a pointer to the allocated memory on success, or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

Applications do not need to use this function unless they are providing
their own [SDL_IOStream](SDL_IOStream) implementation. If you just need an
[SDL_IOStream](SDL_IOStream) to read/write a common data source, you should
use the built-in implementations in SDL, like
[SDL_IOFromFile](SDL_IOFromFile)() or [SDL_IOFromMem](SDL_IOFromMem)(),
etc.

You must free the returned pointer with [SDL_CloseIO](SDL_CloseIO)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CloseIO](SDL_CloseIO)
* [SDL_IOFromConstMem](SDL_IOFromConstMem)
* [SDL_IOFromFile](SDL_IOFromFile)
* [SDL_IOFromMem](SDL_IOFromMem)

----
[CategoryAPI](CategoryAPI)

