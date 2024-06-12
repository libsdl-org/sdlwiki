###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetHintBoolean

Get the boolean value of a hint variable.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
SDL_bool SDL_GetHintBoolean(const char *name, SDL_bool default_value);
```

## Function Parameters

|                      |                   |                                                    |
| -------------------- | ----------------- | -------------------------------------------------- |
| const char *         | **name**          | the name of the hint to get the boolean value from |
| [SDL_bool](SDL_bool) | **default_value** | the value to return if the hint does not exist     |

## Return Value

([SDL_bool](SDL_bool)) Returns the boolean value of a hint or the provided
default value if the hint does not exist.

## Version

This function is available since SDL 2.0.5.

## See Also

- [SDL_GetHint](SDL_GetHint)
- [SDL_SetHint](SDL_SetHint)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)

