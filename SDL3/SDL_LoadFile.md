###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LoadFile

Load all the data from a file path.

## Syntax

```c
void* SDL_LoadFile(const char *file, size_t *datasize);

```

## Function Parameters

|                  |                                                  |
| ---------------- | ------------------------------------------------ |
| **file**         | the path to read all available data from         |
| **datasize**     | if not NULL, will store the number of bytes read |

## Return Value

Returns the data, or NULL if there was an error.

## Remarks

The data is allocated with a zero byte at the end (null terminated) for
convenience. This extra byte is not included in the value reported via
`datasize`.

The data should be freed with [SDL_free](SDL_free)().

Prior to SDL 2.0.10, this function was a macro wrapping around
[SDL_LoadFile_RW](SDL_LoadFile_RW).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

