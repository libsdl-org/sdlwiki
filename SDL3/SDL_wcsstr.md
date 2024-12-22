###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_wcsstr

Search a wide string for the first instance of a specific substring.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
wchar_t * SDL_wcsstr(const wchar_t *haystack, const wchar_t *needle);
```

## Function Parameters

|                 |              |                                                  |
| --------------- | ------------ | ------------------------------------------------ |
| const wchar_t * | **haystack** | the wide string to search. Must not be NULL.     |
| const wchar_t * | **needle**   | the wide string to search for. Must not be NULL. |

## Return Value

(wchar_t *) Returns a pointer to the first instance of `needle` in the
string, or NULL if not found.

## Remarks

The search ends once it finds the requested substring, or a null terminator
byte to end the string.

Note that this looks for strings of _wide characters_, not _codepoints_, so
it's legal to search for malformed and incomplete UTF-16 sequences.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

