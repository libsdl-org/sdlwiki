###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_wcslcpy

Copy a wide string.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_wcslcpy(wchar_t *dst, const wchar_t *src, size_t maxlen);
```

## Function Parameters

|                 |            |                                                                                             |
| --------------- | ---------- | ------------------------------------------------------------------------------------------- |
| wchar_t *       | **dst**    | The destination buffer. Must not be NULL, and must not overlap with `src`.                  |
| const wchar_t * | **src**    | The null-terminated wide string to copy. Must not be NULL, and must not overlap with `dst`. |
| size_t          | **maxlen** | The length (in wide characters) of the destination buffer.                                  |

## Return Value

(size_t) Returns the length (in wide characters, excluding the null
terminator) of `src`.

## Remarks

This function copies `maxlen` - 1 wide characters from `src` to `dst`, then
appends a null terminator.

`src` and `dst` must not overlap.

If `maxlen` is 0, no wide characters are copied and no null terminator is
written.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_wcslcat](SDL_wcslcat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

