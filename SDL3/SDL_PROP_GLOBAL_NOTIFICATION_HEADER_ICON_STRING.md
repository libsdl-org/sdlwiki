# SDL_PROP_GLOBAL_NOTIFICATION_HEADER_ICON_STRING

The path to an image to be used as the header icon for system notifications on some platforms.

## Header File

Defined in [<SDL3/SDL_notification.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_notification.h)

## Syntax

```c
#define SDL_PROP_GLOBAL_NOTIFICATION_HEADER_ICON_STRING "SDL.notification.header_icon"
```

## Remarks

This is required on: - Windows - *nix when not running in a container, and
no .desktop entry is available

Image types supported depend on the platform, but .png generally offers the
best compatability.

On *nix platforms, this can also be the name of a system icon, as specified
by the Icon Naming Specification.

Can be set before calling [SDL_ShowNotification](SDL_ShowNotification)() or
[SDL_ShowSimpleNotification](SDL_ShowSimpleNotification)() for the first
time.

## Version

This macro is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryNotification](CategoryNotification)

