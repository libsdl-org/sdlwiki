###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetMemoryFunctions

Replace SDL's memory allocation functions with a custom set.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_SetMemoryFunctions(SDL_malloc_func malloc_func,
                       SDL_calloc_func calloc_func,
                       SDL_realloc_func realloc_func,
                       SDL_free_func free_func);
```

## Function Parameters

|                                      |                  |                          |
| ------------------------------------ | ---------------- | ------------------------ |
| [SDL_malloc_func](SDL_malloc_func)   | **malloc_func**  | custom malloc function.  |
| [SDL_calloc_func](SDL_calloc_func)   | **calloc_func**  | custom calloc function.  |
| [SDL_realloc_func](SDL_realloc_func) | **realloc_func** | custom realloc function. |
| [SDL_free_func](SDL_free_func)       | **free_func**    | custom free function.    |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

It is not safe to call this function once any allocations have been made,
as future calls to [SDL_free](SDL_free) will use the new allocator, even if
they came from an [SDL_malloc](SDL_malloc) made with the old one!

If used, usually this needs to be the first call made into the SDL library,
if not the very first thing done at program startup time.

## Thread Safety

It is safe to call this function from any thread, but one should not
replace the memory functions once any allocations are made!

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetMemoryFunctions](SDL_GetMemoryFunctions)
- [SDL_GetOriginalMemoryFunctions](SDL_GetOriginalMemoryFunctions)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

