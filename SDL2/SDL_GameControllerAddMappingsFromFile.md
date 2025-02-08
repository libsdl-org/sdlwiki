# SDL_GameControllerAddMappingsFromFile

Load a set of mappings from a file, filtered by the current [SDL_GetPlatform](SDL_GetPlatform)()

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
#define SDL_GameControllerAddMappingsFromFile(file)   SDL_GameControllerAddMappingsFromRW(SDL_RWFromFile(file, "rb"), 1)
```

## Remarks

Convenience macro.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryGameController](CategoryGameController)

