# SDL_GameControllerMappingForIndex

Get the mapping at a particular index.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
char * SDL_GameControllerMappingForIndex(int mapping_index);
```

## Return Value

(char *) Returns the mapping string. Must be freed with
[SDL_free](SDL_free)(). Returns NULL if the index is out of range.

## Version

This function is available since SDL 2.0.6.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

