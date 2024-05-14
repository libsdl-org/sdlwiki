###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryMessagebox](CategoryMessagebox), [CategoryAPIStruct](CategoryAPIStruct), [CategoryVideo](CategoryVideo)


