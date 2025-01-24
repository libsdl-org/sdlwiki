# SDL_strlcat

Concatenate strings.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
size_t SDL_strlcat(char *dst, const char *src, size_t maxlen);
```

## Function Parameters

|              |            |                                                                                                                               |
| ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| char *       | **dst**    | The destination buffer already containing the first null-terminated string. Must not be NULL and must not overlap with `src`. |
| const char * | **src**    | The second null-terminated string. Must not be NULL, and must not overlap with `dst`.                                         |
| size_t       | **maxlen** | The length (in characters) of the destination buffer.                                                                         |

## Return Value

(size_t) Returns the length (in characters, excluding the null terminator)
of the string in `dst` plus the length of `src`.

## Remarks

This function appends up to `maxlen` - [SDL_strlen](SDL_strlen)(dst) - 1
characters from `src` to the end of the string in `dst`, then appends a
null terminator.

`src` and `dst` must not overlap.

If `maxlen` - [SDL_strlen](SDL_strlen)(dst) - 1 is less than or equal to 0,
then `dst` is unmodified.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_strlcpy](SDL_strlcpy)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

