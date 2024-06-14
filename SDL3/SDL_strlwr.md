###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_strlwr

Convert a string to lowercase.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char* SDL_strlwr(char *str);
```

## Function Parameters

|        |         |                                                  |
| ------ | ------- | ------------------------------------------------ |
| char * | **str** | the string to convert in-place. Can not be NULL. |

## Return Value

(char *) Returns the `str` pointer passed into this function.

## Remarks

**WARNING**: Regardless of system locale, this will only convert ASCII
values 'A' through 'Z' to lowercase.

This function operates on a null-terminated string of bytes--even if it is
malformed UTF-8!--and converts ASCII characters 'A' through 'Z' to their
lowercase equivalents in-place, returning the original `str` pointer.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_strupr](SDL_strupr)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

