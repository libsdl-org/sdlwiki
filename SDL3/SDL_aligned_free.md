###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_aligned_free

Free memory allocated by [SDL_aligned_alloc](SDL_aligned_alloc)().

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_aligned_free(void *mem);
```

## Function Parameters

|        |         |                                                                          |
| ------ | ------- | ------------------------------------------------------------------------ |
| void * | **mem** | a pointer previously returned by [SDL_aligned_alloc](SDL_aligned_alloc). |

## Remarks

The pointer is no longer valid after this call and cannot be dereferenced
anymore.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_aligned_alloc](SDL_aligned_alloc)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

