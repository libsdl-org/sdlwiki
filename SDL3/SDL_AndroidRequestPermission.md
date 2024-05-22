###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AndroidRequestPermission

Request permissions at runtime, asynchronously.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
int SDL_AndroidRequestPermission(const char *permission, SDL_AndroidRequestPermissionCallback cb, void *userdata);

```

## Function Parameters

|                    |                                                           |
| ------------------ | --------------------------------------------------------- |
| **permission**     | The permission to request.                                |
| **cb**             | The callback to trigger when the request has a response.  |
| **userdata**       | An app-controlled pointer that is passed to the callback. |

## Return Value

Returns zero if the request was submitted, -1 if there was an error
submitting. The result of the request is only ever reported through the
callback, not this return value.

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

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem), [CategoryAndroid](CategoryAndroid)


