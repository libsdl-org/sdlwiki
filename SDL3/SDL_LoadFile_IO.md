###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LoadFile_IO

Load all the data from an SDL data stream.

## Header File

Defined in [SDL_iostream.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void* SDL_LoadFile_IO(SDL_IOStream *src, size_t *datasize, SDL_bool closeio);

```

## Function Parameters

|                  |                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| **src**          | the [SDL_IOStream](SDL_IOStream) to read all available data from                                                    |
| **datasize**     | if not NULL, will store the number of bytes read                                                                    |
| **closeio**      | if [SDL_TRUE](SDL_TRUE), calls [SDL_CloseIO](SDL_CloseIO)() on `src` before returning, even in the case of an error |

## Return Value

Returns the data, or NULL if there was an error.

## Remarks

The data is allocated with a zero byte at the end (null terminated) for
convenience. This extra byte is not included in the value reported via
`datasize`.

The data should be freed with [SDL_free](SDL_free)().

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_LoadFile](SDL_LoadFile)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

