###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetHint

Set a hint with normal priority.

## Syntax

```c
SDL_bool SDL_SetHint(const char *name,
                     const char *value);

```

## Function Parameters

|               |                                |
| ------------- | ------------------------------ |
| **name**      | the hint to set                |
| **value**     | the value of the hint variable |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the hint was set, [SDL_FALSE](SDL_FALSE.md)
otherwise.

## Remarks

Hints will not be set if there is an existing override hint or environment
variable that takes precedence. You can use
[SDL_SetHintWithPriority](SDL_SetHintWithPriority.md)() to set the hint with
override priority instead.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "1");
```

## Related Functions

* [SDL_GetHint](SDL_GetHint.md)
* [SDL_SetHintWithPriority](SDL_SetHintWithPriority.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryHints](CategoryHints.md)
