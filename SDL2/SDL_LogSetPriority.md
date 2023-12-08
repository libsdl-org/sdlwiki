###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LogSetPriority

Set the priority of a particular log category.

## Syntax

```c
void SDL_LogSetPriority(int category,
                        SDL_LogPriority priority);

```

## Function Parameters

|                  |                                                  |
| ---------------- | ------------------------------------------------ |
| **category**     | the category to assign a priority to             |
| **priority**     | the [SDL_LogPriority](SDL_LogPriority.md) to assign |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LogGetPriority](SDL_LogGetPriority.md)
* [SDL_LogSetAllPriority](SDL_LogSetAllPriority.md)

----
[CategoryAPI](CategoryAPI.md)
