###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ispunct

Report if a character is a punctuation mark.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_ispunct(int x);
```

## Function Parameters

|     |       |                           |
| --- | ----- | ------------------------- |
| int | **x** | character value to check. |

## Return Value

(int) Returns non-zero if x falls within the character class, zero
otherwise.

## Remarks

**WARNING**: Regardless of system locale, this is equivalent to
`((SDL_isgraph(x)) && (!SDL_isalnum(x)))`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_isgraph](SDL_isgraph)
- [SDL_isalnum](SDL_isalnum)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

