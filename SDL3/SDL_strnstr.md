###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_strnstr

Search a string, up to n bytes, for the first instance of a specific substring.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char * SDL_strnstr(const char *haystack, const char *needle, size_t maxlen);
```

## Function Parameters

|              |              |                                                      |
| ------------ | ------------ | ---------------------------------------------------- |
| const char * | **haystack** | the string to search. Must not be NULL.              |
| const char * | **needle**   | the string to search for. Must not be NULL.          |
| size_t       | **maxlen**   | the maximum number of bytes to search in `haystack`. |

## Return Value

(char *) Returns a pointer to the first instance of `needle` in the string,
or NULL if not found.

## Remarks

The search ends once it finds the requested substring, or a null terminator
byte to end the string, or `maxlen` bytes have been examined. It is
possible to use this function on a string without a null terminator.

Note that this looks for strings of _bytes_, not _characters_, so it's
legal to search for malformed and incomplete UTF-8 sequences.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

