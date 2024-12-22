###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_wcsdup

Allocate a copy of a wide string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
wchar_t * SDL_wcsdup(const wchar_t *wstr);
```

## Function Parameters

|                 |          |                     |
| --------------- | -------- | ------------------- |
| const wchar_t * | **wstr** | the string to copy. |

## Return Value

(wchar_t *) Returns a pointer to the newly-allocated wide string.

## Remarks

This allocates enough space for a null-terminated copy of `wstr`, using
[SDL_malloc](SDL_malloc), and then makes a copy of the string into this
space.

The returned string is owned by the caller, and should be passed to
[SDL_free](SDL_free) when no longer needed.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

