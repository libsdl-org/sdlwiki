###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LoadDollarTemplates

Load Dollar Gesture templates from a file.

## Syntax

```c
int SDL_LoadDollarTemplates(SDL_TouchID touchId, SDL_RWops *src);

```

## Function Parameters

|                 |                                       |
| --------------- | ------------------------------------- |
| **touchId**     | a touch id                            |
| **src**         | a [SDL_RWops](SDL_RWops.md) to load from |

## Return Value

Returns the number of loaded templates on success or a negative error code
(or 0) on failure; call [SDL_GetError](SDL_GetError.md)() for more
information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SaveAllDollarTemplates](SDL_SaveAllDollarTemplates.md)
* [SDL_SaveDollarTemplate](SDL_SaveDollarTemplate.md)

----
[CategoryAPI](CategoryAPI.md)
