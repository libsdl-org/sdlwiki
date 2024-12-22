###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_strndup

Allocate a copy of a string, up to n characters.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_strndup(const char *str, size_t maxlen);
```

## Function Parameters

|              |            |                                                                                      |
| ------------ | ---------- | ------------------------------------------------------------------------------------ |
| const char * | **str**    | the string to copy.                                                                  |
| size_t       | **maxlen** | the maximum length of the copied string, not counting the null-terminator character. |

## Return Value

(char *) Returns a pointer to the newly-allocated string.

## Remarks

This allocates enough space for a null-terminated copy of `str`, up to
`maxlen` bytes, using [SDL_malloc](SDL_malloc), and then makes a copy of
the string into this space.

If the string is longer than `maxlen` bytes, the returned string will be
`maxlen` bytes long, plus a null-terminator character that isn't included
in the count.

The returned string is owned by the caller, and should be passed to
[SDL_free](SDL_free) when no longer needed.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

