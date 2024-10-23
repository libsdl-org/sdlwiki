###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_free

Free allocated memory.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_free(void *mem);
```

## Function Parameters

|        |         |                                         |
| ------ | ------- | --------------------------------------- |
| void * | **mem** | a pointer to allocated memory, or NULL. |

## Remarks

The pointer is no longer valid after this call and cannot be dereferenced
anymore.

If `mem` is NULL, this function does nothing.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_malloc](SDL_malloc)
- [SDL_calloc](SDL_calloc)
- [SDL_realloc](SDL_realloc)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

