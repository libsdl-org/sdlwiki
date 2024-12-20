###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_memset

Initialize all bytes of buffer of memory to a specific value.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_memset(void *dst, int c, size_t len);
```

## Function Parameters

|        |         |                                                  |
| ------ | ------- | ------------------------------------------------ |
| void * | **dst** | the destination memory region. Must not be NULL. |
| int    | **c**   | the byte value to set.                           |
| size_t | **len** | the length, in bytes, to set in `dst`.           |

## Return Value

(void *) Returns `dst`.

## Remarks

This function will set `len` bytes, pointed to by `dst`, to the value
specified in `c`.

Despite `c` being an `int` instead of a `char`, this only operates on
bytes; `c` must be a value between 0 and 255, inclusive.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

