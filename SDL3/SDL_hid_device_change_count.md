###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_device_change_count

Check to see if devices may have been added or removed.

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_hid_enumerate](SDL_hid_enumerate)

----
[CategoryAPI](CategoryAPI)

