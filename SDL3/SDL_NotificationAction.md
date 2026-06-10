# SDL_NotificationAction

Notification structure describing actions that can be used to allow users to interact with notification dialogs.

## Header File

Defined in [<SDL3/SDL_notification.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_notification.h)

## Syntax

```c
typedef union SDL_NotificationAction
{
    SDL_NotificationActionType type;

    struct
    {
        SDL_NotificationActionType type; /**< SDL_NOTIFICATION_ACTION_TYPE_BUTTON */
        const char *action_id;           /**< The identifier string for the button. 'default' is a reserved identifier and must not be used. */
        const char *action_label;        /**< The localized label for the button associated with the action, in UTF-8 encoding. */
    } button;

    Uint8 padding[128];
} SDL_NotificationAction;
```

## Remarks

Exactly How they are presented depends on the platform and implementation.

User interactions with a notification are reported via events with the type
[SDL_EVENT_NOTIFICATION_ACTION_INVOKED](SDL_EVENT_NOTIFICATION_ACTION_INVOKED).

Action types: - button: A button with a localized text label, which
generates feedback when activated.

## See Also

- [SDL_NotificationEvent](SDL_NotificationEvent)
- [SDL_NotificationActionType](SDL_NotificationActionType)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryNotification](CategoryNotification)

