###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TextEditingExtEvent

Extended keyboard text editing event structure (event.editExt.*) when text would be truncated if stored in the text buffer [SDL_TextEditingEvent](SDL_TextEditingEvent)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
typedef struct SDL_TextEditingExtEvent
{
    Uint32 type;                                /**< ::SDL_TEXTEDITING_EXT */
    Uint32 timestamp;                           /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 windowID;                            /**< The window with keyboard focus, if any */
    char* text;                                 /**< The editing text, which should be freed with SDL_free(), and will not be NULL */
    Sint32 start;                               /**< The start cursor of selected editing text */
    Sint32 length;                              /**< The length of selected editing text */
} SDL_TextEditingExtEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

