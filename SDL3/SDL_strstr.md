###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_strstr

Search a string for the first instance of a specific substring.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_strstr(const char *haystack, const char *needle);
```

## Function Parameters

|              |              |                                             |
| ------------ | ------------ | ------------------------------------------- |
| const char * | **haystack** | the string to search. Must not be NULL.     |
| const char * | **needle**   | the string to search for. Must not be NULL. |

## Return Value

(char *) Returns a pointer to the first instance of `needle` in the string,
or NULL if not found.

## Remarks

The search ends once it finds the requested substring, or a null terminator
byte to end the string.

Note that this looks for strings of _bytes_, not _characters_, so it's
legal to search for malformed and incomplete UTF-8 sequences.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

