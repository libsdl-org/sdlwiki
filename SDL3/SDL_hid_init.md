====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_hid_init =

Initialize the HIDAPI library.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_hid_init(void);
</syntaxhighlight>

== Return Value ==

Returns 0 on success and -1 on error.

== Remarks ==

This function initializes the HIDAPI library. Calling it is not strictly
necessary, as it will be called automatically by [[SDL_hid_enumerate]]()
and any of the [[SDL_hid_open_]]*() functions if it is needed. This
function should be called at the beginning of execution however, if there
is a chance of HIDAPI handles being opened by different threads
simultaneously.

Each call to this function should have a matching call to
[[SDL_hid_exit]]()

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_hid_exit]]

----
[[CategoryAPI]]


