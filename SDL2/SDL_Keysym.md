###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Keysym

The SDL keysym structure, used in key events.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h)

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

## Data Fields

|                                            |                                                |                                                                     |
| ------------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------- |
| [SDL_Scancode](SDL_Scancode)               | **scancode**                                   | SDL physical key code; see [SDL_Scancode](SDL_Scancode) for details |
| [SDL_Keycode](SDL_Keycode)                 | **sym**                                        | SDL virtual key code; see [SDL_Keycode](SDL_Keycode) for details    |
| Uint16                                     | **mod**                                        | current key modifiers; see [SDL_Keymod](SDL_Keymod) for details     |
| <span style="color:#808080;">Uint32</span> | <span style="color:#808080;">**unused**</span> |                                                                     |

## Related Enumerations

[SDL_Keycode](SDL_Keycode)
[SDL_Keymod](SDL_Keymod)
[SDL_Scancode](SDL_Scancode)

## Related Structures

[SDL_KeyboardEvent](SDL_KeyboardEvent)
[SDL_TextInputEvent](SDL_TextInputEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryKeyboard](CategoryKeyboard)


