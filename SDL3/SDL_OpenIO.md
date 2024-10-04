###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_OpenIO

Create a custom [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
SDL_IOStream * SDL_OpenIO(const SDL_IOStreamInterface *iface, void *userdata);
```

## Function Parameters

|                                                        |              |                                                                                                                                |
| ------------------------------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| const [SDL_IOStreamInterface](SDL_IOStreamInterface) * | **iface**    | the interface that implements this [SDL_IOStream](SDL_IOStream), initialized using [SDL_INIT_INTERFACE](SDL_INIT_INTERFACE)(). |
| void *                                                 | **userdata** | the pointer that will be passed to the interface functions.                                                                    |

## Return Value

([SDL_IOStream](SDL_IOStream) *) Returns a pointer to the allocated memory
on success or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

Applications do not need to use this function unless they are providing
their own [SDL_IOStream](SDL_IOStream) implementation. If you just need an
[SDL_IOStream](SDL_IOStream) to read/write a common data source, you should
use the built-in implementations in SDL, like
[SDL_IOFromFile](SDL_IOFromFile)() or [SDL_IOFromMem](SDL_IOFromMem)(),
etc.

This function makes a copy of `iface` and the caller does not need to keep
it around after this call.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CloseIO](SDL_CloseIO)
- [SDL_INIT_INTERFACE](SDL_INIT_INTERFACE)
- [SDL_IOFromConstMem](SDL_IOFromConstMem)
- [SDL_IOFromFile](SDL_IOFromFile)
- [SDL_IOFromMem](SDL_IOFromMem)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

