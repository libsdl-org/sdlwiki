###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TextInputEvent

Keyboard text input event structure (event.text.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_TextInputEvent
{
    Uint32 type;                              /**< SDL_TEXTINPUT */
    Uint32 timestamp;                         /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 windowID;                          /**< The window with keyboard focus, if any */
    char text[SDL_TEXTINPUTEVENT_TEXT_SIZE];  /**< The input text; UTF-8 encoded. */
} SDL_TextInputEvent;
```

## Remarks

`text` is limited to
[SDL_TEXTINPUTEVENT_TEXT_SIZE](SDL_TEXTINPUTEVENT_TEXT_SIZE) bytes. If the
incoming string is larger than this, SDL will split it and send it in
pieces, across multiple events. The string is in UTF-8 format, and if
split, SDL guarantees that it will not split in the middle of a UTF-8
sequence, so any event will only contain complete codepoints. However, if
there are several codepoints that go together into a single glyph (like an
emoji "thumbs up" followed by a skin color), they may be split between
events.

This event will never be delivered unless text input is enabled by calling
[SDL_StartTextInput](SDL_StartTextInput)(). Text input is enabled by
default on desktop platforms, and disabled by default on mobile platforms!

## See Also

- [SDL_StartTextInput](SDL_StartTextInput)
- [SDL_StopTextInput](SDL_StopTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents), CategoryAPIStruct, CategoryEvents


