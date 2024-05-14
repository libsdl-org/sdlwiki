###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TextEditingEvent

Keyboard text editing event structure (event.edit.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_TextEditingEvent
{
    Uint32 type;                                /**< SDL_TEXTEDITING */
    Uint32 timestamp;                           /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 windowID;                            /**< The window with keyboard focus, if any */
    char text[SDL_TEXTEDITINGEVENT_TEXT_SIZE];  /**< The editing text */
    Sint32 start;                               /**< The start cursor of selected editing text */
    Sint32 length;                              /**< The length of selected editing text */
} SDL_TextEditingEvent;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents), [CategoryAPIStruct](CategoryAPIStruct), 

