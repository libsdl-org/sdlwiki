###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetHint

Get the value of a hint.

## Syntax

```c
const char * SDL_GetHint(const char *name);

```

## Function Parameters

|              |                   |
| ------------ | ----------------- |
| **name**     | the hint to query |

## Return Value

Returns the string value of a hint or NULL if the hint isn't set.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetHint](SDL_SetHint)
* [SDL_SetHintWithPriority](SDL_SetHintWithPriority)

----
[CategoryAPI](CategoryAPI)

