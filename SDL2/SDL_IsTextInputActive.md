###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsTextInputActive

Check whether or not Unicode text input events are enabled.

## Syntax

```c
SDL_bool SDL_IsTextInputActive(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if text input events are enabled else
[SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_StartTextInput](SDL_StartTextInput)

----
[CategoryAPI](CategoryAPI)

