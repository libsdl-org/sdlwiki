###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Keymod

Enumeration of valid key mods (possibly OR'd together).

## Header File

Defined in [SDL_keycode.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keycode.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef enum SDL_Keymod
{
    SDL_KMOD_NONE = 0x0000,    /**< no modifier is applicable. */
    SDL_KMOD_LSHIFT = 0x0001,  /**< the left Shift key is down. */
    SDL_KMOD_RSHIFT = 0x0002,  /**< the right Shift key is down. */
    SDL_KMOD_LCTRL = 0x0040,   /**< the left Ctrl (Control) key is down. */
    SDL_KMOD_RCTRL = 0x0080,   /**< the right Ctrl (Control) key is down. */
    SDL_KMOD_LALT = 0x0100,    /**< the left Alt key is down. */
    SDL_KMOD_RALT = 0x0200,    /**< the right Alt key is down. */
    SDL_KMOD_LGUI = 0x0400,    /**< the left GUI key (often the Windows key) is down. */
    SDL_KMOD_RGUI = 0x0800,    /**< the right GUI key (often the Windows key) is down. */
    SDL_KMOD_NUM = 0x1000,     /**< the Num Lock key (may be located on an extended keypad) is down. */
    SDL_KMOD_CAPS = 0x2000,    /**< the Caps Lock key is down. */
    SDL_KMOD_MODE = 0x4000,    /**< the !AltGr key is down. */
    SDL_KMOD_SCROLL = 0x8000,  /**< the Scoll Lock key is down. */

    SDL_KMOD_CTRL = SDL_KMOD_LCTRL | SDL_KMOD_RCTRL,    /**< Any Ctrl key is down. */
    SDL_KMOD_SHIFT = SDL_KMOD_LSHIFT | SDL_KMOD_RSHIFT, /**< Any Shift key is down. */
    SDL_KMOD_ALT = SDL_KMOD_LALT | SDL_KMOD_RALT,       /**< Any Alt key is down. */
    SDL_KMOD_GUI = SDL_KMOD_LGUI | SDL_KMOD_RGUI,       /**< Any GUI key is down. */

    SDL_KMOD_RESERVED = SDL_KMOD_SCROLL /* This is for source-level compatibility with SDL 2.0.0. */
} SDL_Keymod;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

