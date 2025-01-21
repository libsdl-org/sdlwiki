###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_strdup

Allocate a copy of a string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_strdup(const char *str);
```

## Function Parameters

|              |         |                     |
| ------------ | ------- | ------------------- |
| const char * | **str** | the string to copy. |

## Return Value

(char *) Returns a pointer to the newly-allocated string.

## Remarks

This allocates enough space for a null-terminated copy of `str`, using
[SDL_malloc](SDL_malloc), and then makes a copy of the string into this
space.

The returned string is owned by the caller, and should be passed to
[SDL_free](SDL_free) when no longer needed.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

