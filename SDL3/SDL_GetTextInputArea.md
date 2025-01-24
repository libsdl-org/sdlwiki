# SDL_GetTextInputArea

Get the area used to type Unicode text input.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
bool SDL_GetTextInputArea(SDL_Window *window, SDL_Rect *rect, int *cursor);
```

## Function Parameters

|                            |            |                                                                                            |
| -------------------------- | ---------- | ------------------------------------------------------------------------------------------ |
| [SDL_Window](SDL_Window) * | **window** | the window for which to query the text input area.                                         |
| [SDL_Rect](SDL_Rect) *     | **rect**   | a pointer to an [SDL_Rect](SDL_Rect) filled in with the text input area, may be NULL.      |
| int *                      | **cursor** | a pointer to the offset of the current cursor location relative to `rect->x`, may be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This returns the values previously set by
[SDL_SetTextInputArea](SDL_SetTextInputArea)().

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetTextInputArea](SDL_SetTextInputArea)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

