###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerMappingForIndex

Get the mapping at a particular index.

## Syntax

```c
char * SDL_GameControllerMappingForIndex(int mapping_index);

```

## Return Value

Returns the mapping string. Must be freed with [SDL_free](SDL_free.md)().
Returns NULL if the index is out of range.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI.md)
