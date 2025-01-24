# SDL_EnumerationResult

Possible results from an enumeration callback.

## Header File

Defined in [<SDL3/SDL_filesystem.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_filesystem.h)

## Syntax

```c
typedef enum SDL_EnumerationResult
{
    SDL_ENUM_CONTINUE,   /**< Value that requests that enumeration continue. */
    SDL_ENUM_SUCCESS,    /**< Value that requests that enumeration stop, successfully. */
    SDL_ENUM_FAILURE     /**< Value that requests that enumeration stop, as a failure. */
} SDL_EnumerationResult;
```

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_EnumerateDirectoryCallback](SDL_EnumerateDirectoryCallback)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryFilesystem](CategoryFilesystem)

