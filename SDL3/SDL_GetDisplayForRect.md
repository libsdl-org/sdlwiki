# SDL_GetDisplayForRect

Get the display primarily containing a rect.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_DisplayID SDL_GetDisplayForRect(const SDL_Rect *rect);
```

## Function Parameters

|                              |          |                    |
| ---------------------------- | -------- | ------------------ |
| const [SDL_Rect](SDL_Rect) * | **rect** | the rect to query. |

## Return Value

([SDL_DisplayID](SDL_DisplayID)) Returns the instance ID of the display
entirely containing the rect or closest to the center of the rect on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetDisplayBounds](SDL_GetDisplayBounds)
- [SDL_GetDisplays](SDL_GetDisplays)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

