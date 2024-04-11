###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDLTest_TextWindow

Data used for multi-line text output

## Header File

Defined in [SDL_test_font.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_test_font.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
typedef struct SDLTest_TextWindow
{
    SDL_Rect rect;
    int current;
    int numlines;
    char **lines;
} SDLTest_TextWindow;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

