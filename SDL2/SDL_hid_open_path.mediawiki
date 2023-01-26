====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_hid_open_path =

Open a HID device by its path name.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_hid_device * SDL_hid_open_path(const char *path, int bExclusive /* = false */);
</syntaxhighlight>

== Function Parameters ==

{|
|'''path'''
|The path name of the device to open
|}

== Return Value ==

Returns a pointer to a [[SDL_hid_device]] object on success or NULL on
failure.

== Remarks ==

The path name be determined by calling [[SDL_hid_enumerate]](), or a
platform-specific path name can be used (eg: /dev/hidraw0 on Linux).

== Version ==

This function is available since SDL 2.0.18.

----
[[CategoryAPI]]


