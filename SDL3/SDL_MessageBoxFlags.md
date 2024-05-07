###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MessageBoxFlags

[SDL_MessageBox](SDL_MessageBox) flags.

## Header File

Defined in [<SDL3/SDL_messagebox.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_messagebox.h)

## Syntax

```c
typedef Uint32 SDL_MessageBoxFlags;

#define SDL_MESSAGEBOX_ERROR                    0x00000010u /**< error dialog */
#define SDL_MESSAGEBOX_WARNING                  0x00000020u /**< warning dialog */
#define SDL_MESSAGEBOX_INFORMATION              0x00000040u /**< informational dialog */
#define SDL_MESSAGEBOX_BUTTONS_LEFT_TO_RIGHT    0x00000080u /**< buttons placed left to right */
#define SDL_MESSAGEBOX_BUTTONS_RIGHT_TO_LEFT    0x00000100u /**< buttons placed right to left */
```

## Remarks

If supported will display warning icon, etc.

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryAPIEnum](CategoryAPIEnum)


