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

|              |              |                                                     |
| ------------ | ------------ | --------------------------------------------------- |
| const char * | **message**  | text message to be shown                            |
| int          | **duration** | 0=short, 1=long                                     |
| int          | **gravity**  | where the notification should appear on the screen. |
| int          | **xoffset**  | set this parameter only when gravity >=0            |
| int          | **yoffset**  | set this parameter only when gravity >=0            |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Toasts are a sort of lightweight notification that are unique to Android.

https://developer.android.com/guide/topics/ui/notifiers/toasts

Shows toast in UI thread.

For the `gravity` parameter, choose a value from here, or -1 if you don't
have a preference:

https://developer.android.com/reference/android/view/Gravity

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem), [CategoryAndroid](CategoryAndroid)


