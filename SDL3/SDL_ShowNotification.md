# SDL_ShowNotification

Show a system notification with normal priority.

## Header File

Defined in [<SDL3/SDL_notification.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_notification.h)

## Syntax

```c
SDL_NotificationID SDL_ShowNotification(const char *title, const char *message, SDL_Surface *image, SDL_NotificationAction *actions, int num_actions);
```

## Function Parameters

|                                                    |                 |                                                                 |
| -------------------------------------------------- | --------------- | --------------------------------------------------------------- |
| const char *                                       | **title**       | UTF-8 title text, required.                                     |
| const char *                                       | **message**     | UTF-8 message text, may be NULL.                                |
| [SDL_Surface](SDL_Surface) *                       | **image**       | The image associated with this notification, may be NULL.       |
| [SDL_NotificationAction](SDL_NotificationAction) * | **actions**     | An array of actions to attach to the notification, may be NULL. |
| int                                                | **num_actions** | The number of actions in the actions array.                     |

## Return Value

([SDL_NotificationID](SDL_NotificationID)) Returns A non-zero
[SDL_NotificationID](SDL_NotificationID) on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_ShowNotificationWithProperties](SDL_ShowNotificationWithProperties)
- [SDL_NotificationAction](SDL_NotificationAction)
- [SDL_NotificationEvent](SDL_NotificationEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryNotification](CategoryNotification)

