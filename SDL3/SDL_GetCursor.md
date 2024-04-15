###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_GetCursor

Get the active cursor.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_Cursor* SDL_GetCursor(void);

```

## Return Value

Returns the active cursor or NULL if there is no mouse.

## Remarks

This function returns a pointer to the current cursor which is owned by the
library. It is not necessary to free the cursor with
[SDL_DestroyCursor](SDL_DestroyCursor)().

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_SetCursor](SDL_SetCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse), [CategoryDraft](CategoryDraft)


