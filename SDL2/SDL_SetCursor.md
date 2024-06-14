###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetCursor

Set the active cursor.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h)

## Syntax

```c
void SDL_SetCursor(SDL_Cursor * cursor);
```

## Function Parameters

|                            |            |                          |
| -------------------------- | ---------- | ------------------------ |
| [SDL_Cursor](SDL_Cursor) * | **cursor** | a cursor to make active. |

## Remarks

This function sets the currently active cursor to the specified one. If the
cursor is currently visible, the change will be immediately represented on
the display. [SDL_SetCursor](SDL_SetCursor)(NULL) can be used to force
cursor redraw, if this is desired for any reason.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_GetCursor](SDL_GetCursor)
- [SDL_ShowCursor](SDL_ShowCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

