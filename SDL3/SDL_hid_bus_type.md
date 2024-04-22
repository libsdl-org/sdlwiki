###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_hid_bus_type

HID underlying bus types.

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hidapi.h)

## Syntax

```c
typedef enum SDL_hid_bus_type {
    /** Unknown bus type */
    SDL_HID_API_BUS_UNKNOWN = 0x00,

    /** USB bus
       Specifications:
       https://usb.org/hid */
    SDL_HID_API_BUS_USB = 0x01,

    /** Bluetooth or Bluetooth LE bus
       Specifications:
       https://www.bluetooth.com/specifications/specs/human-interface-device-profile-1-1-1/
       https://www.bluetooth.com/specifications/specs/hid-service-1-0/
       https://www.bluetooth.com/specifications/specs/hid-over-gatt-profile-1-0/ */
    SDL_HID_API_BUS_BLUETOOTH = 0x02,

    /** I2C bus
       Specifications:
       https://docs.microsoft.com/previous-versions/windows/hardware/design/dn642101(v=vs.85) */
    SDL_HID_API_BUS_I2C = 0x03,

    /** SPI bus
       Specifications:
       https://www.microsoft.com/download/details.aspx?id=103325 */
    SDL_HID_API_BUS_SPI = 0x04

} SDL_hid_bus_type;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

