# SDL_toupper

Convert low-ASCII English letters to uppercase.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_toupper(int x);
```

## Function Parameters

|     |       |                           |
| --- | ----- | ------------------------- |
| int | **x** | character value to check. |

## Return Value

(int) Returns capitalized version of x, or x if no conversion available.

## Remarks

**WARNING**: Regardless of system locale, this will only convert ASCII
values 'a' through 'z' to uppercase.

This function returns the uppercase equivalent of `x`. If a character
cannot be converted, or is already uppercase, this function returns `x`.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

