###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_GAMECONTROLLERCONFIG_FILE

A variable that lets you provide a file with extra gamecontroller db entries.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GAMECONTROLLERCONFIG_FILE "SDL_GAMECONTROLLERCONFIG_FILE"
```

## Remarks

The file should contain lines of gamecontroller config data, see
[SDL_gamepad](SDL_gamepad).h

You can update mappings after SDL is initialized with
[SDL_GetGamepadMappingForGUID](SDL_GetGamepadMappingForGUID)() and
[SDL_AddGamepadMapping](SDL_AddGamepadMapping)()

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

