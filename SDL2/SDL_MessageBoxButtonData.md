###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGStructures for details on editing this page*^*^*^*^* -->
# SDL_MessageBoxButtonData

Individual button data.

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_messagebox.h)

## Syntax

```c
typedef struct SDL_MessageBoxButtonData
{
    Uint32 flags;       /**< ::SDL_MessageBoxButtonFlags */
    int buttonid;       /**< User defined button id (value returned via SDL_ShowMessageBox) */
    const char * text;  /**< The UTF-8 button text */
} SDL_MessageBoxButtonData;
```

## Data Fields

|               |               |                                                                                          |
| ------------- | ------------- | ---------------------------------------------------------------------------------------- |
|  Uint32       | **flags**     |  one of the values from [SDL_MessageBoxButtonFlags](SDL_MessageBoxButtonFlags)           |
|  int          | **buttonid**  |  user defined button id (value returned via [SDL_ShowMessageBox](SDL_ShowMessageBox)())  |
|  const char*  | **text**      |  the UTF-8 button text                                                                   |

## Related Enumerations

[SDL_MessageBoxButtonFlags](SDL_MessageBoxButtonFlags)

## Related Structures

[SDL_MessageBoxData](SDL_MessageBoxData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryVideo](CategoryVideo), [CategoryDraft](CategoryDraft)


