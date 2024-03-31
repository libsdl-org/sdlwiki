###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AndroidShowToast

Shows an Android toast notification.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_AndroidShowToast(const char* message, int duration, int gravity, int xoffset, int yoffset);

```

## Function Parameters

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **message**      | text message to be shown                            |
| **duration**     | 0=short, 1=long                                     |
| **gravity**      | where the notification should appear on the screen. |
| **xoffset**      | set this parameter only when gravity >=0            |
| **yoffset**      | set this parameter only when gravity >=0            |

## Return Value

Returns 0 if success, -1 if any error occurs.

## Remarks

Toasts are a sort of lightweight notification that are unique to Android.

https://developer.android.com/guide/topics/ui/notifiers/toasts

Shows toast in UI thread.

For the `gravity` parameter, choose a value from here, or -1 if you don't
have a preference:

https://developer.android.com/reference/android/view/Gravity

## Version

This function is available since SDL 2.0.16.

----
[CategoryAPI](CategoryAPI)

