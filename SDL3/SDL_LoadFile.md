# SDL_LoadFile

Load all the data from a file path.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
void * SDL_LoadFile(const char *file, size_t *datasize);
```

## Function Parameters

|              |              |                                                   |
| ------------ | ------------ | ------------------------------------------------- |
| const char * | **file**     | the path to read all available data from.         |
| size_t *     | **datasize** | if not NULL, will store the number of bytes read. |

## Return Value

(void *) Returns the data or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The data is allocated with a zero byte at the end (null terminated) for
convenience. This extra byte is not included in the value reported via
`datasize`.

The data should be freed with [SDL_free](SDL_free)().

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LoadFile_IO](SDL_LoadFile_IO)
- [SDL_SaveFile](SDL_SaveFile)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

