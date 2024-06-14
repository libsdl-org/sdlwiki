###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_wcscmp

Compare two null-terminated wide strings.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_wcscmp(const wchar_t *str1, const wchar_t *str2);
```

## Function Parameters

|                 |          |                                                      |
| --------------- | -------- | ---------------------------------------------------- |
| const wchar_t * | **str1** | the first string to compare. NULL is not permitted!  |
| const wchar_t * | **str2** | the second string to compare. NULL is not permitted! |

## Return Value

(int) Returns less than zero if str1 is "less than" str2, greater than zero
if str1 is "greater than" str2, and zero if the strings match exactly.

## Remarks

This only compares wchar_t values until it hits a null-terminating
character; it does not care if the string is well-formed UTF-16 (or UTF-32,
depending on your platform's wchar_t size), or uses valid Unicode values.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

