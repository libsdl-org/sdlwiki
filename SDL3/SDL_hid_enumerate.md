====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_hid_enumerate =

Enumerate the HID Devices.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_hid_device_info * SDL_hid_enumerate(unsigned short vendor_id, unsigned short product_id);
</syntaxhighlight>

== Function Parameters ==

{|
|'''vendor_id'''
|The Vendor ID (VID) of the types of device to open.
|-
|'''product_id'''
|The Product ID (PID) of the types of device to open.
|}

== Return Value ==

Returns a pointer to a linked list of type [[SDL_hid_device_info]],
containing information about the HID devices attached to the system, or
NULL in the case of failure. Free this linked list by calling
[[SDL_hid_free_enumeration]]().

== Remarks ==

This function returns a linked list of all the HID devices attached to the
system which match vendor_id and product_id. If <code>vendor_id</code> is
set to 0 then any vendor matches. If <code>product_id</code> is set to 0
then any product matches. If <code>vendor_id</code> and
<code>product_id</code> are both set to 0, then all HID devices will be
returned.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_hid_device_change_count]]

----
[[CategoryAPI]]


