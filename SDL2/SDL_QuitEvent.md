###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_QuitEvent

The "quit requested" event

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_QuitEvent
{
    Uint32 type;        /**< ::SDL_QUIT */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
} SDL_QuitEvent;
```

## Code Examples

```c++
SDL_Event e;
for (;;) {
    SDL_PollEvent(&e);
    if (e.type == SDL_QUIT) {
        SDL_Log("Program quit after %i ticks", e.quit.timestamp);
        break;
    }
}
```

## Data Fields

{|
|Uint32
|'''type'''
|SDL_QUIT
|-
|Uint32
|'''timestamp'''
|timestamp of the event
|}

## Related Enumerations

:[[SDL_EventType]]

## Related Structures

:[[SDL_Event]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


