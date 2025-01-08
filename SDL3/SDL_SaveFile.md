###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SaveFile

Save all the data into a file path.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_SaveFile(const char *file, const void *data, size_t datasize);
```

## Function Parameters

|              |              |                                                                             |
| ------------ | ------------ | --------------------------------------------------------------------------- |
| const char * | **file**     | the path to read all available data from.                                   |
| const void * | **data**     | the data to be written. If datasize is 0, may be NULL or a invalid pointer. |
| size_t       | **datasize** | the number of bytes to be written.                                          |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.1.8.

## See Also

- [SDL_SaveFile_IO](SDL_SaveFile_IO)
- [SDL_LoadFile](SDL_LoadFile)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

