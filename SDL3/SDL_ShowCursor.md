# SDL_ShowCursor

Show the cursor.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
bool SDL_ShowCursor(void);
```

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CursorVisible](SDL_CursorVisible)
- [SDL_HideCursor](SDL_HideCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

