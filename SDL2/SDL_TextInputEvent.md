###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TextInputEvent

Keyboard text input event structure (event.text.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_TextInputEvent
{
    Uint32 type;                              /**< ::SDL_TEXTINPUT */
    Uint32 timestamp;                         /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 windowID;                          /**< The window with keyboard focus, if any */
    char text[SDL_TEXTINPUTEVENT_TEXT_SIZE];  /**< The input text */
} SDL_TextInputEvent;
```

## Data Fields

{|
|Uint32 
|'''type''' 
|SDL_TEXTINPUT 
|-
|Uint32
|'''timestamp'''
|timestamp of the event
|-
|Uint32 
|'''windowID''' 
|the window with keyboard focus, if any 
|-
|char[32] 
|'''text''' 
|the null-terminated input text in UTF-8 encoding 
|}

## Related Enumerations

: [SDL_EventType](SDL_EventType)

## Related Structures

: [SDL_Event](SDL_Event)
: [SDL_TextEditingEvent](SDL_TextEditingEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), CategoryStruct, CategoryEvents


