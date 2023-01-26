====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_hid_read_timeout =

Read an Input report from a HID device with timeout.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_hid_read_timeout(SDL_hid_device *dev, unsigned char *data, size_t length, int milliseconds);
</syntaxhighlight>

== Function Parameters ==

{|
|'''dev'''
|A device handle returned from [[SDL_hid_open]]().
|-
|'''data'''
|A buffer to put the read data into.
|-
|'''length'''
|The number of bytes to read. For devices with multiple reports, make sure to read an extra byte for the report number.
|-
|'''milliseconds'''
|timeout in milliseconds or -1 for blocking wait.
|}

== Return Value ==

Returns the actual number of bytes read and -1 on error. If no packet was
available to be read within the timeout period, this function returns 0.

== Remarks ==

Input reports are returned to the host through the INTERRUPT IN endpoint.
The first byte will contain the Report number if the device uses numbered
reports.

== Version ==

This function is available since SDL 2.0.18.

----
[[CategoryAPI]]


