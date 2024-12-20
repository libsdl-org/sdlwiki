###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_memset4

Initialize all 32-bit words of buffer of memory to a specific value.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_memset4(void *dst, Uint32 val, size_t dwords);
```

## Function Parameters

|                  |            |                                                        |
| ---------------- | ---------- | ------------------------------------------------------ |
| void *           | **dst**    | the destination memory region. Must not be NULL.       |
| [Uint32](Uint32) | **val**    | the [Uint32](Uint32) value to set.                     |
| size_t           | **dwords** | the number of [Uint32](Uint32) values to set in `dst`. |

## Return Value

(void *) Returns `dst`.

## Remarks

This function will set a buffer of `dwords` [Uint32](Uint32) values,
pointed to by `dst`, to the value specified in `val`.

Unlike [SDL_memset](SDL_memset), this sets 32-bit values, not bytes, so
it's not limited to a range of 0-255.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

