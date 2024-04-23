###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGStructures for details on editing this page*^*^*^*^* -->
# SDL_MessageBoxColorScheme

A set of colors to use for message box dialogs

## Header File

Defined in [SDL_messagebox.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_messagebox.h)

## Syntax

```c
typedef struct SDL_MessageBoxColorScheme
{
    SDL_MessageBoxColor colors[SDL_MESSAGEBOX_COLOR_MAX];
} SDL_MessageBoxColorScheme;
```

## Data Fields

|                                               |              |   |
| --------------------------------------------- | ------------ | - |
| [SDL_MessageBoxColor](SDL_MessageBoxColor)[5] | '''colors''' |   |

## Related Enumerations

[SDL_MessageBoxColorType](SDL_MessageBoxColorType)

## Related Structures

[SDL_MessageBoxColor](SDL_MessageBoxColor)
[SDL_MessageBoxData](SDL_MessageBoxData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryVideo](CategoryVideo), [CategoryDraft](CategoryDraft)


