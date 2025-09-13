# SDL_UpperBlit

Perform a fast blit from the source surface to the destination surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_UpperBlit
    (SDL_Surface * src, const SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);
```

## Function Parameters

|                              |             |                                                                                                                                                                                                                                                                                  |
| ---------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **src**     | the [SDL_Surface](SDL_Surface) structure to be copied from.                                                                                                                                                                                                                      |
| const [SDL_Rect](SDL_Rect) * | **srcrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied, or NULL to copy the entire surface.                                                                                                                                                                  |
| [SDL_Surface](SDL_Surface) * | **dst**     | the [SDL_Surface](SDL_Surface) structure that is the blit target.                                                                                                                                                                                                                |
| [SDL_Rect](SDL_Rect) *       | **dstrect** | the [SDL_Rect](SDL_Rect) structure representing the x and y position in the destination surface, or NULL for (0,0). The width and height are ignored, and are copied from `srcrect`. If you want a specific width and height, you should use [SDL_BlitScaled](SDL_BlitScaled)(). |

## Return Value

(int) Returns 0 if the blit is successful or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

[SDL_UpperBlit](SDL_UpperBlit)() has been replaced by
[SDL_BlitSurface](SDL_BlitSurface)(), which is merely a macro for this
function with a less confusing name.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_BlitSurface](SDL_BlitSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

