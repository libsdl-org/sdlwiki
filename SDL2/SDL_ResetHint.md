###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ResetHint

Reset a hint to the default value.

## Syntax

```c
SDL_bool SDL_ResetHint(const char *name);

```

## Function Parameters

|              |                 |
| ------------ | --------------- |
| **name**     | the hint to set |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the hint was set, [SDL_FALSE](SDL_FALSE.md)
otherwise.

## Remarks

This will reset a hint to the value of the environment variable, or NULL if
the environment isn't set. Callbacks will be called normally with this
change.

## Version

This function is available since SDL 2.24.0.

## Related Functions

* [SDL_GetHint](SDL_GetHint.md)
* [SDL_SetHint](SDL_SetHint.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryHints](CategoryHints.md)
