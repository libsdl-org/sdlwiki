# SDL_strrev

Reverse a string's contents.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_strrev(char *str);
```

## Function Parameters

|        |         |                        |
| ------ | ------- | ---------------------- |
| char * | **str** | the string to reverse. |

## Return Value

(char *) Returns `str`.

## Remarks

This reverses a null-terminated string in-place. Only the content of the
string is reversed; the null-terminator character remains at the end of the
reversed string.

**WARNING**: This function reverses the _bytes_ of the string, not the
codepoints. If `str` is a UTF-8 string with Unicode codepoints > 127, this
will ruin the string data. You should only use this function on strings
that are completely comprised of low ASCII characters.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

