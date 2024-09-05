###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_strpbrk

Searches a string for the first occurence of any character contained in a breakset, and returns a pointer from the string to that character.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_strpbrk(const char * SDL_RESTRICT str, const char * SDL_RESTRICT breakset);
```

## Function Parameters

|                                           |              |                                                                         |
| ----------------------------------------- | ------------ | ----------------------------------------------------------------------- |
| const char * [SDL_RESTRICT](SDL_RESTRICT) | **str**      | The null-terminated string to be searched.                              |
| const char * [SDL_RESTRICT](SDL_RESTRICT) | **breakset** | A null-terminated string containing the list of characters to look for. |

## Return Value

(char *) Returns A pointer to the location, in str, of the first occurence
of a character present in the breakset, or NULL if none is found.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

