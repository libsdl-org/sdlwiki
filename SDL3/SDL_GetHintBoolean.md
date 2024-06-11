###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetHintBoolean

Get the boolean value of a hint variable.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
SDL_bool SDL_GetHintBoolean(const char *name, SDL_bool default_value);
```

## Function Parameters

|                       |                                                    |
| --------------------- | -------------------------------------------------- |
| **name**              | the name of the hint to get the boolean value from |
| **default_value**     | the value to return if the hint does not exist     |

## Return Value

Returns the boolean value of a hint or the provided default value if the
hint does not exist.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetHint](SDL_GetHint)
- [SDL_SetHint](SDL_SetHint)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHints](CategoryHints)

