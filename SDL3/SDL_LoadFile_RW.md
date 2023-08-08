###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LoadFile_RW

Load all the data from an SDL data stream.

## Syntax

```c
void* SDL_LoadFile_RW(SDL_RWops *src, size_t *datasize, SDL_bool freesrc);

```

## Function Parameters

|                  |                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- |
| **src**          | the [SDL_RWops](SDL_RWops) to read all available data from                                                          |
| **datasize**     | if not NULL, will store the number of bytes read                                                                    |
| **freesrc**      | if [SDL_TRUE](SDL_TRUE), calls [SDL_RWclose](SDL_RWclose)() on `src` before returning, even in the case of an error |

## Return Value

Returns the data, or NULL if there was an error.

## Remarks

The data is allocated with a zero byte at the end (null terminated) for
convenience. This extra byte is not included in the value reported via
`datasize`.

The data should be freed with [SDL_free](SDL_free)().

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

