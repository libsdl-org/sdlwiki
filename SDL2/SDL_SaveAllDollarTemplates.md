# SDL_SaveAllDollarTemplates

Save all currently loaded Dollar Gesture templates.

## Header File

Defined in [SDL_gesture.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gesture.h)

## Syntax

```c
int SDL_SaveAllDollarTemplates(SDL_RWops *dst);
```

## Function Parameters

|                          |         |                                      |
| ------------------------ | ------- | ------------------------------------ |
| [SDL_RWops](SDL_RWops) * | **dst** | a [SDL_RWops](SDL_RWops) to save to. |

## Return Value

(int) Returns the number of saved templates on success or 0 on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_LoadDollarTemplates](SDL_LoadDollarTemplates)
- [SDL_SaveDollarTemplate](SDL_SaveDollarTemplate)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGesture](CategoryGesture)

