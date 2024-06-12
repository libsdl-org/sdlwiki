###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ResetHint

Reset a hint to the default value.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
SDL_bool SDL_ResetHint(const char *name);
```

## Function Parameters

|              |          |                 |
| ------------ | -------- | --------------- |
| const char * | **name** | the hint to set |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the hint was set,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This will reset a hint to the value of the environment variable, or NULL if
the environment isn't set. Callbacks will be called normally with this
change.

## Version

This function is available since SDL 2.24.0.

## See Also

- [SDL_GetHint](SDL_GetHint)
- [SDL_SetHint](SDL_SetHint)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)

