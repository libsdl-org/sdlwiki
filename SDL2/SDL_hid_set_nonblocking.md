###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_set_nonblocking

Set the device handle to be non-blocking.

## Syntax

```c
int SDL_hid_set_nonblocking(SDL_hid_device *dev, int nonblock);

```

## Function Parameters

|                  |                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------- |
| **dev**          | A device handle returned from [SDL_hid_open](SDL_hid_open)().                             |
| **nonblock**     | enable or not the nonblocking reads - 1 to enable nonblocking - 0 to disable nonblocking. |

## Return Value

Returns 0 on success and -1 on error.

## Remarks

In non-blocking mode calls to [SDL_hid_read](SDL_hid_read)() will return
immediately with a value of 0 if there is no data to be read. In blocking
mode, [SDL_hid_read](SDL_hid_read)() will wait (block) until there is data
to read before returning.

Nonblocking can be turned on and off at any time.

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI)

