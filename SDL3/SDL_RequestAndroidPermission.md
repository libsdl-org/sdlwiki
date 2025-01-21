###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_RequestAndroidPermission

Request permissions at runtime, asynchronously.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
bool SDL_RequestAndroidPermission(const char *permission, SDL_RequestAndroidPermissionCallback cb, void *userdata);
```

## Function Parameters

|                                                                              |                |                                                           |
| ---------------------------------------------------------------------------- | -------------- | --------------------------------------------------------- |
| const char *                                                                 | **permission** | the permission to request.                                |
| [SDL_RequestAndroidPermissionCallback](SDL_RequestAndroidPermissionCallback) | **cb**         | the callback to trigger when the request has a response.  |
| void *                                                                       | **userdata**   | an app-controlled pointer that is passed to the callback. |

## Return Value

(bool) Returns true if the request was submitted, false if there was an
error submitting. The result of the request is only ever reported through
the callback, not this return value.

## Remarks

You do not need to call this for built-in functionality of SDL; recording
from a microphone or reading images from a camera, using standard SDL APIs,
will manage permission requests for you.

This function never blocks. Instead, the app-supplied callback will be
called when a decision has been made. This callback may happen on a
different thread, and possibly much later, as it might wait on a user to
respond to a system dialog. If permission has already been granted for a
specific entitlement, the callback will still fire, probably on the current
thread and before this function returns.

If the request submission fails, this function returns -1 and the callback
will NOT be called, but this should only happen in catastrophic conditions,
like memory running out. Normally there will be a yes or no to the request
through the callback.

For the `permission` parameter, choose a value from here:

https://developer.android.com/reference/android/Manifest.permission

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

