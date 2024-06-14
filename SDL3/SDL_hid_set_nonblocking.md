###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_set_nonblocking

Set the device handle to be non-blocking.

## Header File

Defined in [<SDL3/SDL_hidapi.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hidapi.h)

## Syntax

```c
int SDL_hid_set_nonblocking(SDL_hid_device *dev, int nonblock);
```

## Function Parameters

|                                    |              |                                                                                           |
| ---------------------------------- | ------------ | ----------------------------------------------------------------------------------------- |
| [SDL_hid_device](SDL_hid_device) * | **dev**      | a device handle returned from [SDL_hid_open](SDL_hid_open)().                             |
| int                                | **nonblock** | enable or not the nonblocking reads - 1 to enable nonblocking - 0 to disable nonblocking. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

In non-blocking mode calls to [SDL_hid_read](SDL_hid_read)() will return
immediately with a value of 0 if there is no data to be read. In blocking
mode, [SDL_hid_read](SDL_hid_read)() will wait (block) until there is data
to read before returning.

Nonblocking can be turned on and off at any time.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryHIDAPI](CategoryHIDAPI)

