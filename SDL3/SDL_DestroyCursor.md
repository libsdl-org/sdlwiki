# SDL_DestroyCursor

Free a previously-created cursor.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
void SDL_DestroyCursor(SDL_Cursor *cursor);
```

## Function Parameters

|                            |            |                     |
| -------------------------- | ---------- | ------------------- |
| [SDL_Cursor](SDL_Cursor) * | **cursor** | the cursor to free. |

## Remarks

Use this function to free cursor resources created with
[SDL_CreateCursor](SDL_CreateCursor)(),
[SDL_CreateColorCursor](SDL_CreateColorCursor)() or
[SDL_CreateSystemCursor](SDL_CreateSystemCursor)().

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateColorCursor](SDL_CreateColorCursor)
- [SDL_CreateCursor](SDL_CreateCursor)
- [SDL_CreateSystemCursor](SDL_CreateSystemCursor)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

