# SDL_ShowNotificationWithProperties

Show a system notification.

## Header File

Defined in [<SDL3/SDL_notification.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_notification.h)

## Syntax

```c
SDL_NotificationID SDL_ShowNotificationWithProperties(SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                                                            |
| ------------------------------------ | --------- | ---------------------------------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to be used when creating this notification. |

## Return Value

([SDL_NotificationID](SDL_NotificationID)) Returns A non-zero
[SDL_NotificationID](SDL_NotificationID) on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

System notifications are small, asynchronous popup windows that notify the
user of some information. How they are displayed is system dependent.

These are the supported properties:

- [`SDL_PROP_NOTIFICATION_TITLE_STRING`](SDL_PROP_NOTIFICATION_TITLE_STRING):
  the title of the notification, in UTF-8 encoding. This property is
  required.
- [`SDL_PROP_NOTIFICATION_ACTIONS_POINTER`](SDL_PROP_NOTIFICATION_ACTIONS_POINTER):
  An array of pointers to
  [`SDL_NotificationAction`](SDL_NotificationAction) structs that will add
  actions to the notification, usually in the form of buttons or menu
  items. Note that systems may have a limit on the maximum number of
  actions that a notification can have.
- [`SDL_PROP_NOTIFICATIONS_ACTION_COUNT_NUMBER`](SDL_PROP_NOTIFICATIONS_ACTION_COUNT_NUMBER):
  the number of actions in the array of actions, if it exists.
- [`SDL_PROP_NOTIFICATION_IMAGE_POINTER`](SDL_PROP_NOTIFICATION_IMAGE_POINTER):
  a pointer to an [`SDL_Surface`](SDL_Surface) containing an image that
  will be attached to the notification. In most cases, the image is
  displayed in the form of a large icon or thumbnail alongside the message
  body. Notifications on Apple platforms can be expanded to show a larger
  format image.
- [`SDL_PROP_NOTIFICATION_MESSAGE_STRING`](SDL_PROP_NOTIFICATION_MESSAGE_STRING):
  the message body of the notification, in UTF-8 encoding.
- [`SDL_PROP_NOTIFICATION_PRIORITY_NUMBER`](SDL_PROP_NOTIFICATION_PRIORITY_NUMBER):
  an [`SDL_NotificationPriority`](SDL_NotificationPriority) value
  representing the notification priority.
- [`SDL_PROP_NOTIFICATION_REPLACES_NUMBER`](SDL_PROP_NOTIFICATION_REPLACES_NUMBER):
  the [`SDL_NotificationID`](SDL_NotificationID) of a previously shown
  notification that this notification should replace.
- [`SDL_PROP_NOTIFICATION_SOUND_STRING`](SDL_PROP_NOTIFICATION_SOUND_STRING):
  sets a sound to play when the notification is shown. This can have the
  value "default", to play the system default notification sound, "silent",
  to play no sound, or contain the path to a file with a custom sound. The
  paths and formats that can be used for custom sounds are system-specific,
  and can have some restrictions, depending on the platform:
- Apple platforms require that the sound file is contained within the app
  bundle. Supported formats are: Linear PCM, MA4 (IMA/ADPCM), uLaw, or
  aLaw, in an .aiff, .wav, or .caf file.
- Windows can only play custom notification sounds when the app is packaged
  inside an MSIX installer. Playback from arbitrary file paths is not
  supported. Supported formats are: .aac, .flac, .m4a, .mp3, .wav, and
  .wma.
- Unix platforms can generally load sounds from any arbitrary path, as long
  as the read permissions are correct. Supported formats are: ogg/opus,
  ogg/vorbis, and wav/pcm. If this property is not set, the system default
  sound will be used.
- [`SDL_PROP_NOTIFICATION_TRANSIENT_BOOLEAN`](SDL_PROP_NOTIFICATION_TRANSIENT_BOOLEAN):
  true if the notification should not persist in the system notification
  center after initially being shown.

Not all properties are supported by all platforms.

Notifications are available on: - Windows 10 or higher - macOS 10.14 or
higher - iOS 11 or higher - *nix platforms that support the
org.freedesktop.Notifications, or org.freedesktop.portal.Notification
interfaces

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_ShowNotification](SDL_ShowNotification)
- [SDL_NotificationAction](SDL_NotificationAction)
- [SDL_NotificationPriority](SDL_NotificationPriority)
- [SDL_NotificationEvent](SDL_NotificationEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryNotification](CategoryNotification)

