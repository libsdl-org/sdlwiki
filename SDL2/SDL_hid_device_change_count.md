###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_device_change_count

Check to see if devices may have been added or removed.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
Uint32 SDL_hid_device_change_count(void);

```

## Return Value

Returns a change counter that is incremented with each potential device
change, or 0 if device change detection isn't available.

## Remarks

Enumerating the HID devices is an expensive operation, so you can call this
to see if there have been any system device changes since the last call to
this function. A change in the counter returned doesn't necessarily mean
that anything has changed, but you can call
[SDL_hid_enumerate](SDL_hid_enumerate)() to get an updated device list.

Calling this function for the first time may cause a thread or other system
resource to be allocated to track device change notifications.

## Version

This function is available since SDL 2.0.18.

## See Also

* [SDL_hid_enumerate](SDL_hid_enumerate)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

