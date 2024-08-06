###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetKeyFromScancode

Get the key code that would be sent with the given scancode in a key event.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
SDL_Keycode SDL_GetKeyFromScancode(SDL_Scancode scancode, SDL_Keymod modstate);
```

## Function Parameters

|                              |              |                                                                       |
| ---------------------------- | ------------ | --------------------------------------------------------------------- |
| [SDL_Scancode](SDL_Scancode) | **scancode** | the [SDL_Scancode](SDL_Scancode) to translate.                        |
| [SDL_Keymod](SDL_Keymod)     | **modstate** | the modifier state to use when translating the scancode to a keycode. |

## Return Value

([SDL_Keycode](SDL_Keycode)) Returns the [SDL_Keycode](SDL_Keycode) that
corresponds to the given [SDL_Scancode](SDL_Scancode).

## Remarks

This uses the information from the current keymap along with the options
specified in [SDL_HINT_KEYCODE_OPTIONS](SDL_HINT_KEYCODE_OPTIONS) to get
the keycode that would be delivered to the application in a key event. This
is typically the unmodified version of the key based on the current
keyboard layout. For example, the keycode for
[SDL_SCANCODE_A](SDL_SCANCODE_A) + [SDL_KMOD_SHIFT](SDL_KMOD_SHIFT) using
the US QWERTY layout would be 'a'.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

