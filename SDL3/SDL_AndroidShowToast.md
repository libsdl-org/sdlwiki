###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AndroidShowToast

Shows an Android toast notification.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

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

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Toasts are a sort of lightweight notification that are unique to Android.

https://developer.android.com/guide/topics/ui/notifiers/toasts

Shows toast in UI thread.

For the `gravity` parameter, choose a value from here, or -1 if you don't
have a preference:

https://developer.android.com/reference/android/view/Gravity

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAndroid](CategoryAndroid)

