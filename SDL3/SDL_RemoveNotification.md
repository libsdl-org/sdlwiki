# SDL_RemoveNotification

Remove a notification.

## Header File

Defined in [<SDL3/SDL_notification.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_notification.h)

## Syntax

```c
bool SDL_RemoveNotification(SDL_NotificationID notification);
```

## Function Parameters

|                                          |                  |                                       |
| ---------------------------------------- | ---------------- | ------------------------------------- |
| [SDL_NotificationID](SDL_NotificationID) | **notification** | the ID of the notification to remove. |

## Return Value

(bool) Returns True on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.6.0

## See Also

- [SDL_ShowNotificationWithProperties](SDL_ShowNotificationWithProperties)
- [SDL_ShowNotification](SDL_ShowNotification)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryNotification](CategoryNotification)

