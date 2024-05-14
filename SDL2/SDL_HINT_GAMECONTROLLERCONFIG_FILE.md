###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_GAMECONTROLLERCONFIG_FILE

A variable that lets you provide a file with extra gamecontroller db entries.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GAMECONTROLLERCONFIG_FILE "SDL_GAMECONTROLLERCONFIG_FILE"
```

## Remarks

The file should contain lines of gamecontroller config data, see
[SDL_gamecontroller](SDL_gamecontroller).h

This hint must be set before calling
[SDL_Init](SDL_Init)([SDL_INIT_GAMECONTROLLER](SDL_INIT_GAMECONTROLLER))
You can update mappings after the system is initialized with
[SDL_GameControllerMappingForGUID](SDL_GameControllerMappingForGUID)() and
[SDL_GameControllerAddMapping](SDL_GameControllerAddMapping)()

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

