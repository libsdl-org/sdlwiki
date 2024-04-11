###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TextEditingEvent

Keyboard text editing event structure (event.edit.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef struct SDL_TextEditingEvent
{
    SDL_EventType type; /**< ::SDL_EVENT_TEXT_EDITING */
    Uint32 reserved;
    Uint64 timestamp;   /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID; /**< The window with keyboard focus, if any */
    char *text;         /**< The editing text */
    Sint32 start;       /**< The start cursor of selected editing text */
    Sint32 length;      /**< The length of selected editing text */
} SDL_TextEditingEvent;
```

## Remarks

The `text` is owned by SDL and should be copied if the application wants to
hold onto it beyond the scope of handling this event.

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

