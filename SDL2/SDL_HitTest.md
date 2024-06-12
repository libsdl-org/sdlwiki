###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HitTest

Callback used for hit-testing.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
typedef SDL_HitTestResult (SDLCALL *SDL_HitTest)(SDL_Window *win, const SDL_Point *area, void *data);
```

## Function Parameters

|          |                                                                                      |
| -------- | ------------------------------------------------------------------------------------ |
| **win**  | the [SDL_Window](SDL_Window) where hit-testing was set on                            |
| **area** | an [SDL_Point](SDL_Point) which should be hit-tested                                 |
| **data** | what was passed as `callback_data` to [SDL_SetWindowHitTest](SDL_SetWindowHitTest)() |

## Return Value

Return an [SDL_HitTestResult](SDL_HitTestResult) value.

## See Also

- [SDL_SetWindowHitTest](SDL_SetWindowHitTest)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryVideo](CategoryVideo)

