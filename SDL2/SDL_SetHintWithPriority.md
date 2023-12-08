###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetHintWithPriority

Set a hint with a specific priority.

## Syntax

```c
SDL_bool SDL_SetHintWithPriority(const char *name,
                                 const char *value,
                                 SDL_HintPriority priority);

```

## Function Parameters

|                  |                                                             |
| ---------------- | ----------------------------------------------------------- |
| **name**         | the hint to set                                             |
| **value**        | the value of the hint variable                              |
| **priority**     | the [SDL_HintPriority](SDL_HintPriority.md) level for the hint |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the hint was set, [SDL_FALSE](SDL_FALSE.md)
otherwise.

## Remarks

The priority controls the behavior when setting a hint that already has a
value. Hints will replace existing hints of their priority and lower.
Environment variables are considered to have override priority.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetHint](SDL_GetHint.md)
* [SDL_SetHint](SDL_SetHint.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryHints](CategoryHints.md)
