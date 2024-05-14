###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Keymod

Valid key modifiers (possibly OR'd together).

## Header File

Defined in [<SDL3/SDL_keycode.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keycode.h)

## Syntax

```c
typedef Uint16 SDL_Keymod;

#define SDL_KMOD_NONE   0x0000u /**< no modifier is applicable. */
#define SDL_KMOD_LSHIFT 0x0001u /**< the left Shift key is down. */
#define SDL_KMOD_RSHIFT 0x0002u /**< the right Shift key is down. */
#define SDL_KMOD_LCTRL  0x0040u /**< the left Ctrl (Control) key is down. */
#define SDL_KMOD_RCTRL  0x0080u /**< the right Ctrl (Control) key is down. */
#define SDL_KMOD_LALT   0x0100u /**< the left Alt key is down. */
#define SDL_KMOD_RALT   0x0200u /**< the right Alt key is down. */
#define SDL_KMOD_LGUI   0x0400u /**< the left GUI key (often the Windows key) is down. */
#define SDL_KMOD_RGUI   0x0800u /**< the right GUI key (often the Windows key) is down. */
#define SDL_KMOD_NUM    0x1000u /**< the Num Lock key (may be located on an extended keypad) is down. */
#define SDL_KMOD_CAPS   0x2000u /**< the Caps Lock key is down. */
#define SDL_KMOD_MODE   0x4000u /**< the !AltGr key is down. */
#define SDL_KMOD_SCROLL 0x8000u /**< the Scoll Lock key is down. */
#define SDL_KMOD_CTRL   (SDL_KMOD_LCTRL | SDL_KMOD_RCTRL)   /**< Any Ctrl key is down. */
#define SDL_KMOD_SHIFT  (SDL_KMOD_LSHIFT | SDL_KMOD_RSHIFT) /**< Any Shift key is down. */
#define SDL_KMOD_ALT    (SDL_KMOD_LALT | SDL_KMOD_RALT)     /**< Any Alt key is down. */
#define SDL_KMOD_GUI    (SDL_KMOD_LGUI | SDL_KMOD_RGUI)     /**< Any GUI key is down. */

#endif /* SDL_keycode_h_ */
```

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryKeycode](CategoryKeycode)

