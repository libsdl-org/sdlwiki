# SDL_NotificationEvent

Notification dialog event structure (event.notification.*)

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef struct SDL_NotificationEvent
{
    SDL_EventType type; /**< SDL_EVENT_NOTIFICATION_ACTION_INVOKED */
    Uint32 reserved;
    Uint64 timestamp;         /**< In nanoseconds, populated using SDL_GetTicksNS() */
    SDL_NotificationID which; /**< The ID of the notification that generated this event. */
    const char *action_id;    /**< The identifier string of the action invoked in the notification dialog. */
} SDL_NotificationEvent;
```

## Remarks

An `action_id` value of 'default' for an
[SDL_EVENT_NOTIFICATION_ACTION_INVOKED](SDL_EVENT_NOTIFICATION_ACTION_INVOKED)
event indicates that the notification was interacted with without selecting
a specific action (e.g. the body of the notification was clicked on).

## Version

This struct is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

