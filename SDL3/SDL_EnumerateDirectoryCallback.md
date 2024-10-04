###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_EnumerateDirectoryCallback

Callback for directory enumeration.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
typedef SDL_EnumerationResult (SDLCALL *SDL_EnumerateDirectoryCallback)(void *userdata, const char *dirname, const char *fname);
```

## Function Parameters

|              |                                                           |
| ------------ | --------------------------------------------------------- |
| **userdata** | an app-controlled pointer that is passed to the callback. |
| **dirname**  | the directory that is being enumerated.                   |
| **fname**    | the next entry in the enumeration.                        |

## Return Value

Returns how the enumeration should proceed.

## Remarks

Enumeration of directory entries will continue until either all entries
have been provided to the callback, or the callback has requested a stop
through its return value.

Returning [SDL_ENUM_CONTINUE](SDL_ENUM_CONTINUE) will let enumeration
proceed, calling the callback with further entries.
[SDL_ENUM_SUCCESS](SDL_ENUM_SUCCESS) and
[SDL_ENUM_FAILURE](SDL_ENUM_FAILURE) will terminate the enumeration early,
and dictate the return value of the enumeration function itself.

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_EnumerateDirectory](SDL_EnumerateDirectory)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryFilesystem](CategoryFilesystem)

