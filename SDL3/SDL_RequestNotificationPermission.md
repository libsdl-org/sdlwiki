# SDL_RequestNotificationPermission

Requests permission from the system to display notifications.

## Header File

Defined in [<SDL3/SDL_notification.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_notification.h)

## Syntax

```c
bool SDL_RequestNotificationPermission(void);
```

## Return Value

(bool) Returns True on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

A return value of `true` only means that the system supports notifications,
and that the request for permission was successfully issued. It does not
reflect any user settings to allow or deny notifications.

## Version

This function is available since SDL 3.6.0

## See Also

- [SDL_ShowNotification](SDL_ShowNotification)
- [SDL_ShowNotificationWithProperties](SDL_ShowNotificationWithProperties)
- [SDL_NotificationAction](SDL_NotificationAction)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryNotification](CategoryNotification)

