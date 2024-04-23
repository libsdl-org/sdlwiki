###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Keysym

The SDL keysym structure, used in key events.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h)

## Syntax

```c
typedef struct SDL_Keysym
{
    SDL_Scancode scancode;      /**< SDL physical key code - see SDL_Scancode for details */
    SDL_Keycode sym;            /**< SDL virtual key code - see SDL_Keycode for details */
    Uint16 mod;                 /**< current key modifiers */
    Uint32 unused;
} SDL_Keysym;
```

## Remarks

If you are looking for translated character input, see the
[SDL_TEXTINPUT](SDL_TEXTINPUT) event.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryKeyboard](CategoryKeyboard)


