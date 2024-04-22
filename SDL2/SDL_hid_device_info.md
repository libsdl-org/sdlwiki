###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_hid_device_info

Information about a connected HID device

## Header File

Defined in [SDL_hidapi.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hidapi.h)

## Syntax

```c
typedef struct SDL_hid_device_info
{
    /** Platform-specific device path */
    char *path;
    /** Device Vendor ID */
    unsigned short vendor_id;
    /** Device Product ID */
    unsigned short product_id;
    /** Serial Number */
    wchar_t *serial_number;
    /** Device Release Number in binary-coded decimal,
        also known as Device Version Number */
    unsigned short release_number;
    /** Manufacturer String */
    wchar_t *manufacturer_string;
    /** Product string */
    wchar_t *product_string;
    /** Usage Page for this Device/Interface
        (Windows/Mac only). */
    unsigned short usage_page;
    /** Usage for this Device/Interface
        (Windows/Mac only).*/
    unsigned short usage;
    /** The USB interface which this logical device
        represents.

        * Valid on both Linux implementations in all cases.
        * Valid on the Windows implementation only if the device
          contains more than one interface. */
    int interface_number;

    /** Additional information about the USB interface.
        Valid on libusb and Android implementations. */
    int interface_class;
    int interface_subclass;
    int interface_protocol;

    /** Pointer to the next device */
    struct SDL_hid_device_info *next;
} SDL_hid_device_info;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

