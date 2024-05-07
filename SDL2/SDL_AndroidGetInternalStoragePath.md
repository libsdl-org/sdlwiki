###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AndroidGetInternalStoragePath

Get the path used for internal storage for this application.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
const char * SDL_AndroidGetInternalStoragePath(void);

```

## Return Value

Returns the path used for internal storage or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This path is unique to your application and cannot be written to by other
applications.

Your internal storage path is typically:
`/data/data/your.app.package/files`.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AndroidGetExternalStorageState](SDL_AndroidGetExternalStorageState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

