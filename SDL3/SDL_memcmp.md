# SDL_memcmp

Compare two buffers of memory.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_memcmp(const void *s1, const void *s2, size_t len);
```

## Function Parameters

|              |         |                                                      |
| ------------ | ------- | ---------------------------------------------------- |
| const void * | **s1**  | the first buffer to compare. NULL is not permitted!  |
| const void * | **s2**  | the second buffer to compare. NULL is not permitted! |
| size_t       | **len** | the number of bytes to compare between the buffers.  |

## Return Value

(int) Returns less than zero if s1 is "less than" s2, greater than zero if
s1 is "greater than" s2, and zero if the buffers match exactly for `len`
bytes.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

