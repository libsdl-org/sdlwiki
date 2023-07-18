###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReloadGamepadMappings

Reinitialize the SDL mapping database to its initial state.

## Syntax

```c
int SDL_ReloadGamepadMappings(void);

```

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This will generate gamepad events as needed if device mappings change.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

