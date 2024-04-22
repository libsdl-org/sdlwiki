###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RWread

Read from a data source.

## Header File

Defined in [SDL_rwops.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rwops.h)

## Syntax

```c
size_t SDL_RWread(SDL_RWops *context,
                  void *ptr, size_t size,
                  size_t maxnum);

```

## Function Parameters

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **context**     | a pointer to an [SDL_RWops](SDL_RWops) structure |
| **ptr**         | a pointer to a buffer to read data into          |
| **size**        | the size of each object to read, in bytes        |
| **maxnum**      | the maximum number of objects to be read         |

## Return Value

Returns the number of objects read, or 0 at error or end of file; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function reads up to `maxnum` objects each of size `size` from the
data source to the area pointed at by `ptr`. This function may read less
objects than requested. It will return zero when there has been an error or
the data stream is completely read.

[SDL_RWread](SDL_RWread)() is actually a function wrapper that calls the
[SDL_RWops](SDL_RWops)'s `read` method appropriately, to simplify
application development.

Prior to SDL 2.0.10, this function was a macro.

## Version

This function is available since SDL 2.0.10.

## See Also

* [SDL_RWclose](SDL_RWclose)
* [SDL_RWFromConstMem](SDL_RWFromConstMem)
* [SDL_RWFromFile](SDL_RWFromFile)
* [SDL_RWFromFP](SDL_RWFromFP)
* [SDL_RWFromMem](SDL_RWFromMem)
* [SDL_RWseek](SDL_RWseek)
* [SDL_RWwrite](SDL_RWwrite)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

