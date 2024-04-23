###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UserEvent

A user-defined event type (event.user.*)

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef struct SDL_UserEvent
{
    Uint32 type;        /**< ::SDL_USEREVENT through ::SDL_LASTEVENT-1 */
    Uint32 timestamp;   /**< In milliseconds, populated using SDL_GetTicks() */
    Uint32 windowID;    /**< The associated window if any */
    Sint32 code;        /**< User defined event code */
    void *data1;        /**< User defined data pointer */
    void *data2;        /**< User defined data pointer */
} SDL_UserEvent;
```

## Code Examples

```c
Sint32 my_event_code;
void *significant_data;

Uint32 myEventType = SDL_RegisterEvents(1);
if (myEventType != ((Uint32)-1)) {
    SDL_Event event;
    SDL_memset(&event, 0, sizeof(event)); /* or SDL_zero(event) */
    event.type = myEventType;
    event.user.code = my_event_code;
    event.user.data1 = significant_data;
    event.user.data2 = 0;
    SDL_PushEvent(&event);
}
```

## Data Fields

|        |               |                                                                |
| ------ | ------------- | -------------------------------------------------------------- |
| Uint32 | **type**      | value obtained from [SDL_RegisterEvents](SDL_RegisterEvents)() |
| Uint32 | **timestamp** | timestamp of the event                                         |
| Uint32 | **windowID**  | the associated window, if any                                  |
| Sint32 | **code**      | user defined event code                                        |
| void*  | **data1**     | user defined data pointer                                      |
| void*  | **data2**     | user defined data pointer                                      |

## Related Enumerations

[SDL_EventType](SDL_EventType)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


