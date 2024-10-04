###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetCursor

Set the active cursor.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
bool SDL_SetCursor(SDL_Cursor *cursor);
```

## Function Parameters

|                            |            |                          |
| -------------------------- | ---------- | ------------------------ |
| [SDL_Cursor](SDL_Cursor) * | **cursor** | a cursor to make active. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function sets the currently active cursor to the specified one. If the
cursor is currently visible, the change will be immediately represented on
the display. [SDL_SetCursor](SDL_SetCursor)(NULL) can be used to force
cursor redraw, if this is desired for any reason.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetCursor](SDL_GetCursor)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

