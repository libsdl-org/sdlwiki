###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_calloc_func

A callback used to implement [SDL_calloc](SDL_calloc)().

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef void *(SDLCALL *SDL_calloc_func)(size_t nmemb, size_t size);
```

## Function Parameters

|           |                                        |
| --------- | -------------------------------------- |
| **nmemb** | the number of elements in the array.   |
| **size**  | the size of each element of the array. |

## Return Value

Returns a pointer to the allocated array, or NULL if allocation failed.

## Remarks

SDL will always ensure that the passed `nmemb` and `size` are both greater
than 0.

## Thread Safety

It should be safe to call this callback from any thread.

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_calloc](SDL_calloc)
- [SDL_GetOriginalMemoryFunctions](SDL_GetOriginalMemoryFunctions)
- [SDL_GetMemoryFunctions](SDL_GetMemoryFunctions)
- [SDL_SetMemoryFunctions](SDL_SetMemoryFunctions)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

