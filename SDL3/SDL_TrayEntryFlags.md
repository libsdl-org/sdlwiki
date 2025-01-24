# SDL_TrayEntryFlags

Flags that control the creation of system tray entries.

## Header File

Defined in [<SDL3/SDL_tray.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_tray.h)

## Syntax

```c
typedef Uint32 SDL_TrayEntryFlags;

#define SDL_TRAYENTRY_BUTTON      0x00000001u /**< Make the entry a simple button. Required. */
#define SDL_TRAYENTRY_CHECKBOX    0x00000002u /**< Make the entry a checkbox. Required. */
#define SDL_TRAYENTRY_SUBMENU     0x00000004u /**< Prepare the entry to have a submenu. Required */
#define SDL_TRAYENTRY_DISABLED    0x80000000u /**< Make the entry disabled. Optional. */
#define SDL_TRAYENTRY_CHECKED     0x40000000u /**< Make the entry checked. This is valid only for checkboxes. Optional. */
```

## Remarks

Some of these flags are required; exactly one of them must be specified at
the time a tray entry is created. Other flags are optional; zero or more of
those can be OR'ed together with the required flag.

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_InsertTrayEntryAt](SDL_InsertTrayEntryAt)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryTray](CategoryTray)

