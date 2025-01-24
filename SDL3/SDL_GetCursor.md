# SDL_GetCursor

Get the active cursor.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
SDL_Cursor * SDL_GetCursor(void);
```

## Return Value

([SDL_Cursor](SDL_Cursor) *) Returns the active cursor or NULL if there is
no mouse.

## Remarks

This function returns a pointer to the current cursor which is owned by the
library. It is not necessary to free the cursor with
[SDL_DestroyCursor](SDL_DestroyCursor)().

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetCursor](SDL_SetCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

