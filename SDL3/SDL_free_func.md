###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_free_func

A callback used to implement [SDL_free](SDL_free)().

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef void (SDLCALL *SDL_free_func)(void *mem);
```

## Function Parameters

|         |                                |
| ------- | ------------------------------ |
| **mem** | a pointer to allocated memory. |

## Remarks

SDL will always ensure that the passed `mem` is a non-NULL pointer.

## Thread Safety

It should be safe to call this callback from any thread.

## Version

This datatype is available since SDL 3.1.3.

## See Also

- [SDL_free](SDL_free)
- [SDL_GetOriginalMemoryFunctions](SDL_GetOriginalMemoryFunctions)
- [SDL_GetMemoryFunctions](SDL_GetMemoryFunctions)
- [SDL_SetMemoryFunctions](SDL_SetMemoryFunctions)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

