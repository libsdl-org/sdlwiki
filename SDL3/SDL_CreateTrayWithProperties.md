# SDL_CreateTrayWithProperties

Create an icon to be placed in the operating system's tray, or equivalent.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
SDL_Tray * SDL_CreateTrayWithProperties(SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                        |
| ------------------------------------ | --------- | ---------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to use. |

## Return Value

([SDL_Tray](SDL_Tray) *) Returns The newly created system tray icon.

## Remarks

Many platforms advise not using a system tray unless persistence is a
necessary feature. Avoid needlessly creating a tray icon, as the user may
feel like it clutters their interface.

Using tray icons require the video subsystem.

These are the supported properties:

- [`SDL_PROP_TRAY_CREATE_ICON_POINTER`](SDL_PROP_TRAY_CREATE_ICON_POINTER):
  an [SDL_Surface](SDL_Surface) to be used as the tray icon. May be NULL.
- [`SDL_PROP_TRAY_CREATE_TOOLTIP_STRING`](SDL_PROP_TRAY_CREATE_TOOLTIP_STRING):
  a tooltip to be displayed when the mouse hovers the icon in UTF-8
  encoding. Not supported on all platforms. May be NULL.
- [`SDL_PROP_TRAY_CREATE_USERDATA_POINTER`](SDL_PROP_TRAY_CREATE_USERDATA_POINTER):
  an optional pointer to associate with the tray, which will be passed to
  click callbacks. May be NULL.
- [`SDL_PROP_TRAY_CREATE_LEFTCLICK_CALLBACK_POINTER`](SDL_PROP_TRAY_CREATE_LEFTCLICK_CALLBACK_POINTER):
  an [SDL_TrayClickCallback](SDL_TrayClickCallback) to be invoked when the
  tray icon is left-clicked. Not supported on all platforms. The callback
  should return true to show the default menu, or false to skip showing it.
  May be NULL.
- [`SDL_PROP_TRAY_CREATE_RIGHTCLICK_CALLBACK_POINTER`](SDL_PROP_TRAY_CREATE_RIGHTCLICK_CALLBACK_POINTER):
  an [SDL_TrayClickCallback](SDL_TrayClickCallback) to be invoked when the
  tray icon is right-clicked. Not supported on all platforms. The callback
  should return true to show the default menu, or false to skip showing it.
  May be NULL.
- [`SDL_PROP_TRAY_CREATE_MIDDLECLICK_CALLBACK_POINTER`](SDL_PROP_TRAY_CREATE_MIDDLECLICK_CALLBACK_POINTER):
  an [SDL_TrayClickCallback](SDL_TrayClickCallback) to be invoked when the
  tray icon is middle-clicked. Not supported on all platforms. May be NULL.
- [`SDL_PROP_TRAY_CREATE_DOUBLECLICK_CALLBACK_POINTER`](SDL_PROP_TRAY_CREATE_DOUBLECLICK_CALLBACK_POINTER):
  an [SDL_TrayClickCallback](SDL_TrayClickCallback) to be invoked when the
  tray icon is double-clicked. Not supported on all platforms. May be NULL.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.6.0.

## See Also

- [SDL_CreateTray](SDL_CreateTray)
- [SDL_CreateTrayMenu](SDL_CreateTrayMenu)
- [SDL_GetTrayMenu](SDL_GetTrayMenu)
- [SDL_DestroyTray](SDL_DestroyTray)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTray](CategoryTray)

