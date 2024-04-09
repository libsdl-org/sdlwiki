###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_APP_ID

A variable setting the app ID string.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_APP_ID      "SDL_APP_ID"
```

## Remarks

This string is used by desktop compositors to identify and group windows
together, as well as match applications with associated desktop settings
and icons.

On Wayland this corresponds to the "app ID" window property and on X11 this
corresponds to the WM_CLASS property. Windows inherit the value of this
hint at creation time. Changing this hint after a window has been created
will not change the app ID or class of existing windows.

For *nix platforms, this string should be formatted in reverse-DNS notation
and follow some basic rules to be valid:

- The application ID must be composed of two or more elements separated by
  a period (.) character.
- Each element must contain one or more of the alphanumeric characters
  (A-Z, a-z, 0-9) plus underscore (_) and hyphen (-) and must not start
  with a digit. Note that hyphens, while technically allowed, should not be
  used if possible, as they are not supported by all components that use
  the ID, such as D-Bus. For maximum compatibility, replace hyphens with an
  underscore.
- The empty string is not a valid element (ie: your application ID may not
  start or end with a period and it is not valid to have two periods in a
  row).
- The entire ID must be less than 255 characters in length.

Examples of valid app ID strings:

- org.MyOrg.MyApp
- com.your_company.your_app

Desktops such as GNOME and KDE require that the app ID string matches your
application's .desktop file name (e.g. if the app ID string is
'org.MyOrg.MyApp', your application's .desktop file should be named
'org.MyOrg.MyApp.desktop').

If you plan to package your application in a container such as Flatpak, the
app ID should match the name of your Flatpak container as well.

If not set, SDL will attempt to use the application executable name. If the
executable name cannot be retrieved, the generic string
"[SDL_App](SDL_App)" will be used.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

