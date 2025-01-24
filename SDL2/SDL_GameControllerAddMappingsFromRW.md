# SDL_GameControllerAddMappingsFromRW

Load a set of Game Controller mappings from a seekable SDL data stream.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerAddMappingsFromRW(SDL_RWops * rw, int freerw);
```

## Function Parameters

|                          |            |                                                |
| ------------------------ | ---------- | ---------------------------------------------- |
| [SDL_RWops](SDL_RWops) * | **rw**     | the data stream for the mappings to be added.  |
| int                      | **freerw** | non-zero to close the stream after being read. |

## Return Value

(int) Returns the number of mappings added or -1 on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can call this function several times, if needed, to load different
database files.

If a new mapping is loaded for an already known controller GUID, the later
version will overwrite the one currently loaded.

If this function is called before [SDL_Init](SDL_Init), SDL will generate
an [SDL_CONTROLLERDEVICEADDED](SDL_CONTROLLERDEVICEADDED) event for
matching controllers that are plugged in at the time that
[SDL_Init](SDL_Init) is called.

Mappings not belonging to the current platform or with no platform field
specified will be ignored (i.e. mappings for Linux will be ignored in
Windows, etc).

This function will load the text database entirely in memory before
processing it, so take this into consideration if you are in a memory
constrained environment.

## Version

This function is available since SDL 2.0.2.

## See Also

- [SDL_GameControllerAddMapping](SDL_GameControllerAddMapping)
- [SDL_GameControllerAddMappingsFromFile](SDL_GameControllerAddMappingsFromFile)
- [SDL_GameControllerMappingForGUID](SDL_GameControllerMappingForGUID)
- [SDL_CONTROLLERDEVICEADDED](SDL_CONTROLLERDEVICEADDED)


## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

