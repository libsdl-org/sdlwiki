###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetTextInputRect

Set the rectangle used to type Unicode text inputs.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_SetTextInputRect(const SDL_Rect *rect);

```

## Function Parameters

|              |                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------- |
| **rect**     | the [SDL_Rect](SDL_Rect) structure representing the rectangle to receive text (ignored if NULL) |

## Remarks

Native input methods will place a window with word suggestions near it,
without covering the text being inputted.

To start text input in a given location, this function is intended to be
called before [SDL_StartTextInput](SDL_StartTextInput), although some
platforms support moving the rectangle even while text input (and a
composition) is active.

Note: If you want to use the system native IME window, try setting hint
**[SDL_HINT_IME_SHOW_UI](SDL_HINT_IME_SHOW_UI)** to **1**, otherwise this
function won't give you any feedback.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_StartTextInput](SDL_StartTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

