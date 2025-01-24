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

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_HideCursor](SDL_HideCursor)
- [SDL_ShowCursor](SDL_ShowCursor)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

