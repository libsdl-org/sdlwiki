###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ResetHints

Reset all hints to the default values.

## Syntax

```c
void SDL_ResetHints(void);

```

## Remarks

This will reset all hints to the value of the associated environment
variable, or NULL if the environment isn't set. Callbacks will be called
normally with this change.

## Version

This function is available since SDL 2.26.0.

## Related Functions

* [SDL_GetHint](SDL_GetHint)
* [SDL_SetHint](SDL_SetHint)
* [SDL_ResetHint](SDL_ResetHint)

----
[CategoryAPI](CategoryAPI), [CategoryHints](CategoryHints)


