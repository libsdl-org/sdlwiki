###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_MessageBoxButtonData

Individual button data.

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_messagebox.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef struct SDL_MessageBoxButtonData
{
    Uint32 flags;       /**< ::SDL_MessageBoxButtonFlags */
    int buttonID;       /**< User defined button id (value returned via SDL_ShowMessageBox) */
    const char *text;   /**< The UTF-8 button text */
} SDL_MessageBoxButtonData;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

