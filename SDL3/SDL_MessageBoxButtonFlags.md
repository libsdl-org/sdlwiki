###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MessageBoxButtonFlags

Flags for [SDL_MessageBoxButtonData](SDL_MessageBoxButtonData).

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_messagebox.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef enum SDL_MessageBoxButtonFlags
{
    SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT = 0x00000001,  /**< Marks the default button when return is hit */
    SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT = 0x00000002   /**< Marks the default button when escape is hit */
} SDL_MessageBoxButtonFlags;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

