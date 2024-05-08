###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MessageBoxButtonFlags

[SDL_MessageBoxButtonData](SDL_MessageBoxButtonData) flags.

## Header File

Defined in [<SDL3/SDL_messagebox.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_messagebox.h)

## Syntax

```c
typedef Uint32 SDL_MessageBoxButtonFlags;

#define SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT 0x00000001u /**< Marks the default button when return is hit */
#define SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT 0x00000002u /**< Marks the default button when escape is hit */
```

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

