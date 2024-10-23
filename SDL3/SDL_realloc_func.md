###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_realloc_func

A callback used to implement [SDL_realloc](SDL_realloc)().

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef void *(SDLCALL *SDL_realloc_func)(void *mem, size_t size);
```

## Function Parameters

|          |                                                       |
| -------- | ----------------------------------------------------- |
| **mem**  | a pointer to allocated memory to reallocate, or NULL. |
| **size** | the new size of the memory.                           |

## Return Value

Returns a pointer to the newly allocated memory, or NULL if allocation
failed.

## Remarks

SDL will always ensure that the passed `size` is greater than 0.

## Thread Safety

It should be safe to call this callback from any thread.

## Version

This datatype is available since SDL 3.1.3.

## See Also

- [SDL_realloc](SDL_realloc)
- [SDL_GetOriginalMemoryFunctions](SDL_GetOriginalMemoryFunctions)
- [SDL_GetMemoryFunctions](SDL_GetMemoryFunctions)
- [SDL_SetMemoryFunctions](SDL_SetMemoryFunctions)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

