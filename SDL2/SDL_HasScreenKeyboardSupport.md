###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasScreenKeyboardSupport

Check whether the platform has screen keyboard support.

## Syntax

```c
SDL_bool SDL_HasScreenKeyboardSupport(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the platform has some screen keyboard
support or [SDL_FALSE](SDL_FALSE.md) if not.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_StartTextInput](SDL_StartTextInput.md)
* [SDL_IsScreenKeyboardShown](SDL_IsScreenKeyboardShown.md)

----
[CategoryAPI](CategoryAPI.md)
