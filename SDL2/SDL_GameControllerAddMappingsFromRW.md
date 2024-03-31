###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerAddMappingsFromRW

Load a set of Game Controller mappings from a seekable SDL data stream.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_GameControllerAddMappingsFromRW(SDL_RWops * rw, int freerw);

```

## Function Parameters

|                |                                               |
| -------------- | --------------------------------------------- |
| **rw**         | the data stream for the mappings to be added  |
| **freerw**     | non-zero to close the stream after being read |

## Return Value

Returns the number of mappings added or -1 on error; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can call this function several times, if needed, to load different
database files.

If a new mapping is loaded for an already known controller GUID, the later
version will overwrite the one currently loaded.

Mappings not belonging to the current platform or with no platform field
specified will be ignored (i.e. mappings for Linux will be ignored in
Windows, etc).

This function will load the text database entirely in memory before
processing it, so take this into consideration if you are in a memory
constrained environment.

## Version

This function is available since SDL 2.0.2.

## Related Functions

* [SDL_GameControllerAddMapping](SDL_GameControllerAddMapping)
* [SDL_GameControllerAddMappingsFromFile](SDL_GameControllerAddMappingsFromFile)
* [SDL_GameControllerMappingForGUID](SDL_GameControllerMappingForGUID)

----
[CategoryAPI](CategoryAPI)

