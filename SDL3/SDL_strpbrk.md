# SDL_strpbrk

Searches a string for the first occurrence of any character contained in a breakset, and returns a pointer from the string to that character.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_strpbrk(const char *str, const char *breakset);
```

## Function Parameters

|              |              |                                                                                                                            |
| ------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| const char * | **str**      | The null-terminated string to be searched. Must not be NULL, and must not overlap with `breakset`.                         |
| const char * | **breakset** | A null-terminated string containing the list of characters to look for. Must not be NULL, and must not overlap with `str`. |

## Return Value

(char *) Returns A pointer to the location, in str, of the first occurrence
of a character present in the breakset, or NULL if none is found.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

