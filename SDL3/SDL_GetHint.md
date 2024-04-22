###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetHint

Get the value of a hint.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

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

This function is available since SDL 3.0.0.

## See Also

* [SDL_SetHint](SDL_SetHint)
* [SDL_SetHintWithPriority](SDL_SetHintWithPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)


