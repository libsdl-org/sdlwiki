###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AddGamepadMappingsFromFile

Load a set of gamepad mappings from a file.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
int SDL_AddGamepadMappingsFromFile(const char *file);
```

## Function Parameters

|              |                           |
| ------------ | ------------------------- |
| **file**     | the mappings file to load |

## Return Value

Returns the number of mappings added or -1 on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can call this function several times, if needed, to load different
database files.

If a new mapping is loaded for an already known gamepad GUID, the later
version will overwrite the one currently loaded.

Mappings not belonging to the current platform or with no platform field
specified will be ignored (i.e. mappings for Linux will be ignored in
Windows, etc).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AddGamepadMapping](SDL_AddGamepadMapping)
- [SDL_AddGamepadMappingsFromIO](SDL_AddGamepadMappingsFromIO)
- [SDL_GetGamepadMapping](SDL_GetGamepadMapping)
- [SDL_GetGamepadMappingForGUID](SDL_GetGamepadMappingForGUID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

