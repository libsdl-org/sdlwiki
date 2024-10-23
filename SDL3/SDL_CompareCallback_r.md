###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CompareCallback_r

A callback used with SDL sorting and binary search functions.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef int (SDLCALL *SDL_CompareCallback_r)(void *userdata, const void *a, const void *b);
```

## Function Parameters

|              |                                                     |
| ------------ | --------------------------------------------------- |
| **userdata** | the `userdata` pointer passed to the sort function. |
| **a**        | a pointer to the first element being compared.      |
| **b**        | a pointer to the second element being compared.     |

## Return Value

Returns -1 if `a` should be sorted before `b`, 1 if `b` should be sorted
before `a`, 0 if they are equal. If two elements are equal, their order in
the sorted array is undefined.

## Version

This callback is available since SDL 3.1.3.

## See Also

- [SDL_qsort_r](SDL_qsort_r)
- [SDL_bsearch_r](SDL_bsearch_r)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

