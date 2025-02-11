# SDL_MessageBoxButtonData

Individual button data.

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_messagebox.h)

## Syntax

```c
typedef struct SDL_MessageBoxButtonData
{
    Uint32 flags;       /**< SDL_MessageBoxButtonFlags */
    int buttonid;       /**< User defined button id (value returned via SDL_ShowMessageBox) */
    const char * text;  /**< The UTF-8 button text */
} SDL_MessageBoxButtonData;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryMessagebox](CategoryMessagebox)

