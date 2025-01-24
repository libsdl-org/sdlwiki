# SDL_QuitEvent

The "quit requested" event

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_QuitEvent
{
    Uint32 type;        /**< SDL_QUIT */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
} SDL_QuitEvent;
```





----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

