###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_malloc_func

A callback used to implement [SDL_malloc](SDL_malloc)().

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef void *(SDLCALL *SDL_malloc_func)(size_t size);
```

## Function Parameters

|          |                       |
| -------- | --------------------- |
| **size** | the size to allocate. |

## Return Value

Returns a pointer to the allocated memory, or NULL if allocation failed.

## Remarks

SDL will always ensure that the passed `size` is greater than 0.

## Thread Safety

It should be safe to call this callback from any thread.

## Version

This datatype is available since SDL 3.1.3.

## See Also

- [SDL_malloc](SDL_malloc)
- [SDL_GetOriginalMemoryFunctions](SDL_GetOriginalMemoryFunctions)
- [SDL_GetMemoryFunctions](SDL_GetMemoryFunctions)
- [SDL_SetMemoryFunctions](SDL_SetMemoryFunctions)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

