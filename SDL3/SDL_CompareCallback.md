###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CompareCallback

A callback used with SDL sorting and binary search functions.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef int (SDLCALL *SDL_CompareCallback)(const void *a, const void *b);
```

## Function Parameters

|       |                                                 |
| ----- | ----------------------------------------------- |
| **a** | a pointer to the first element being compared.  |
| **b** | a pointer to the second element being compared. |

## Return Value

Returns -1 if `a` should be sorted before `b`, 1 if `b` should be sorted
before `a`, 0 if they are equal. If two elements are equal, their order in
the sorted array is undefined.

## Version

This callback is available since SDL 3.0.0.

## See Also

- [SDL_bsearch](SDL_bsearch)
- [SDL_qsort](SDL_qsort)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

