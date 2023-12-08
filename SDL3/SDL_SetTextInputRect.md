###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_SetTextInputRect

Set the rectangle used to type Unicode text inputs.

## Syntax

```c
int SDL_SetTextInputRect(const SDL_Rect *rect);

```

## Function Parameters

|              |                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------- |
| **rect**     | the [SDL_Rect](SDL_Rect.md) structure representing the rectangle to receive text (ignored if NULL) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Native input methods will place a window with word suggestions near it,
without covering the text being inputted.

To start text input in a given location, this function is intended to be
called before [SDL_StartTextInput](SDL_StartTextInput.md), although some
platforms support moving the rectangle even while text input (and a
composition) is active.

Note: If you want to use the system native IME window, try setting hint
**[SDL_HINT_IME_SHOW_UI](SDL_HINT_IME_SHOW_UI.md)** to **1**, otherwise this
function won't give you any feedback.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_StartTextInput](SDL_StartTextInput.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryKeyboard](CategoryKeyboard.md), [CategoryDraft](CategoryDraft.md)
