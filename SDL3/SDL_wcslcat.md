###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_wcslcat

Concatenate wide strings.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_wcslcat(wchar_t *dst, const wchar_t *src, size_t maxlen);
```

## Function Parameters

|                 |            |                                                                                                                                    |
| --------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| wchar_t *       | **dst**    | The destination buffer already containing the first null-terminated wide string. Must not be NULL and must not overlap with `src`. |
| const wchar_t * | **src**    | The second null-terminated wide string. Must not be NULL, and must not overlap with `dst`.                                         |
| size_t          | **maxlen** | The length (in wide characters) of the destination buffer.                                                                         |

## Return Value

(size_t) Returns the length (in wide characters, excluding the null
terminator) of the string in `dst` plus the length of `src`.

## Remarks

This function appends up to `maxlen` - [SDL_wcslen](SDL_wcslen)(dst) - 1
wide characters from `src` to the end of the wide string in `dst`, then
appends a null terminator.

`src` and `dst` must not overlap.

If `maxlen` - [SDL_wcslen](SDL_wcslen)(dst) - 1 is less than or equal to 0,
then `dst` is unmodified.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_wcslcpy](SDL_wcslcpy)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

