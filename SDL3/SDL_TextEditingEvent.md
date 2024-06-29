###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TextEditingEvent

Keyboard text editing event structure (event.edit.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_TextEditingEvent
{
    SDL_EventType type;         /**< SDL_EVENT_TEXT_EDITING */
    Uint32 reserved;
    Uint64 timestamp;           /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID;      /**< The window with keyboard focus, if any */
    const char *text;           /**< The editing text */
    Sint32 start;               /**< The start cursor of selected editing text, or -1 if not set */
    Sint32 length;              /**< The length of selected editing text, or -1 if not set */
} SDL_TextEditingEvent;
```

## Remarks

The start cursor is the position, in UTF-8 characters, where new typing
will be inserted into the editing text. The length is the number of UTF-8
characters that will be replaced by new typing.

The text string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

