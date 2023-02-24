====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_hid_free_enumeration =

Free an enumeration Linked List 

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_hid_free_enumeration(SDL_hid_device_info *devs);
</syntaxhighlight>

== Function Parameters ==

{|
|'''devs'''
|Pointer to a list of struct_device returned from [[SDL_hid_enumerate]]().
|}

== Remarks ==

This function frees a linked list created by [[SDL_hid_enumerate]]().

== Version ==

This function is available since SDL 2.0.18.

----
[[CategoryAPI]]


