###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_SetCursor

Set the active cursor.

## Syntax

```c
int SDL_SetCursor(SDL_Cursor * cursor);

```

## Function Parameters

|                |                         |
| -------------- | ----------------------- |
| **cursor**     | a cursor to make active |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function sets the currently active cursor to the specified one. If the
cursor is currently visible, the change will be immediately represented on
the display. [SDL_SetCursor](SDL_SetCursor.md)(NULL) can be used to force
cursor redraw, if this is desired for any reason.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
You can add your code example here
```

## Related Functions

* [SDL_CreateCursor](SDL_CreateCursor.md)
* [SDL_GetCursor](SDL_GetCursor.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMouse](CategoryMouse.md), [CategoryDraft](CategoryDraft.md)
