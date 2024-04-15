###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Keysym

The SDL keysym structure, used in key events.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef struct SDL_Keysym
{
    SDL_Scancode scancode;      /**< SDL physical key code - see ::SDL_Scancode for details */
    SDL_Keycode sym;            /**< SDL virtual key code - see ::SDL_Keycode for details */
    Uint16 mod;                 /**< current key modifiers */
    Uint32 unused;
} SDL_Keysym;
```

## Remarks

If you are looking for translated character input, see the
::[SDL_EVENT_TEXT_INPUT](SDL_EVENT_TEXT_INPUT) event.

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

