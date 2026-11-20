# SDL_HINT_DBUS_PREFER_PORTALS

A variable that controls whether D-Bus portal interfaces are preferred over non-portal interfaces.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_DBUS_PREFER_PORTALS "SDL_DBUS_PREFER_PORTALS"
```

## Remarks

Some functionality in SDL (screensaver inhibition and notifications) uses
D-Bus interfaces that have both a portal, and non-portal interface. When
not running in a secure sandbox, SDL will first attempt to use the
non-portal interface, then fall back to the portal interface if the former
is unavailable. In a known secure sandbox environment, such as Flatpak or
Snap, SDL will first attempt to use the portal interface. When enabled,
this hint forces SDL to attempt using the portal interface first, even when
not running in a known secure sandbox environment.

This is intended for debugging, and should not be enabled by default in
shipping applications and games.

The variable can be set to the following values:

- "0": The appropriate interface will be auto-detected (default)
- "1": Portal interfaces will be preferred, even when not running in a
  secure sandbox

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

