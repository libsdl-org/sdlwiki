# SDL_UpperBlitScaled

Perform a scaled surface copy to a destination surface.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
int SDL_UpperBlitScaled
    (SDL_Surface * src, const SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);


#define SDL_BlitScaled SDL_UpperBlitScaled
```

## Function Parameters

|                              |             |                                                                                                                             |
| ---------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Surface](SDL_Surface) * | **src**     | the [SDL_Surface](SDL_Surface) structure to be copied from.                                                                 |
| const [SDL_Rect](SDL_Rect) * | **srcrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be copied, or NULL to copy the entire surface.             |
| [SDL_Surface](SDL_Surface) * | **dst**     | the [SDL_Surface](SDL_Surface) structure that is the blit target.                                                           |
| [SDL_Rect](SDL_Rect) *       | **dstrect** | the [SDL_Rect](SDL_Rect) structure representing the rectangle that is copied into, or NULL to copy into the entire surface. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

[SDL_UpperBlitScaled](SDL_UpperBlitScaled)() has been replaced by
[SDL_BlitScaled](SDL_BlitScaled)(), which is merely a macro for this
function with a less confusing name.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_BlitScaled](SDL_BlitScaled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySurface](CategorySurface)

