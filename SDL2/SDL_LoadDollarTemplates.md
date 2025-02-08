# SDL_LoadDollarTemplates

Load Dollar Gesture templates from a file.

## Header File

Defined in [SDL_gesture.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gesture.h)

## Syntax

```c
int SDL_LoadDollarTemplates(SDL_TouchID touchId, SDL_RWops *src);
```

## Function Parameters

|                            |             |                                        |
| -------------------------- | ----------- | -------------------------------------- |
| [SDL_TouchID](SDL_TouchID) | **touchId** | a touch id.                            |
| [SDL_RWops](SDL_RWops) *   | **src**     | a [SDL_RWops](SDL_RWops) to load from. |

## Return Value

(int) Returns the number of loaded templates on success or a negative error
code (or 0) on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SaveAllDollarTemplates](SDL_SaveAllDollarTemplates)
- [SDL_SaveDollarTemplate](SDL_SaveDollarTemplate)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGesture](CategoryGesture)

