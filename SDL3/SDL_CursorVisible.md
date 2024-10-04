###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CursorVisible

Return whether the cursor is currently being shown.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
bool SDL_CursorVisible(void);
```

## Return Value

(bool) Returns `true` if the cursor is being shown, or `false` if the
cursor is hidden.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_HideCursor](SDL_HideCursor)
- [SDL_ShowCursor](SDL_ShowCursor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

