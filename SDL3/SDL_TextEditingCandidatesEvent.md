###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_TextEditingCandidatesEvent

Keyboard IME candidates event structure (event.edit_candidates.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_TextEditingCandidatesEvent
{
    SDL_EventType type;         /**< SDL_EVENT_TEXT_EDITING_CANDIDATES */
    Uint32 reserved;
    Uint64 timestamp;           /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_WindowID windowID;      /**< The window with keyboard focus, if any */
    const char * const *candidates;    /**< The list of candidates, or NULL if there are no candidates available */
    Sint32 num_candidates;      /**< The number of strings in `candidates` */
    Sint32 selected_candidate;  /**< The index of the selected candidate, or -1 if no candidate is selected */
    bool horizontal;          /**< true if the list is horizontal, false if it's vertical */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_TextEditingCandidatesEvent;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

