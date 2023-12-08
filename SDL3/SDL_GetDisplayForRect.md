###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetDisplayForRect

Get the display primarily containing a rect.

## Syntax

```c
SDL_DisplayID SDL_GetDisplayForRect(const SDL_Rect *rect);

```

## Function Parameters

|              |                   |
| ------------ | ----------------- |
| **rect**     | the rect to query |

## Return Value

Returns the instance ID of the display entirely containing the rect or
closest to the center of the rect on success or 0 on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetDisplayBounds](SDL_GetDisplayBounds.md)
* [SDL_GetDisplays](SDL_GetDisplays.md)

----
[CategoryAPI](CategoryAPI.md)
