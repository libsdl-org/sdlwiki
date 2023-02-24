====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_iPhoneSetAnimationCallback =

Use this function to set the animation callback on Apple iOS.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_iPhoneSetAnimationCallback(SDL_Window * window, int interval, void (SDLCALL *callback)(void*), void *callbackParam);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window for which the animation callback should be set
|-
|'''interval'''
|the number of frames after which '''callback''' will be called
|-
|'''callback'''
|the function to call for every frame.
|-
|'''callbackParam'''
|a pointer that is passed to <code>callback</code>.
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

The function prototype for <code>callback</code> is:

<syntaxhighlight lang='c'>
void callback(void* callbackParam);
</syntaxhighlight>

Where its parameter, <code>callbackParam</code>, is what was passed as
<code>callbackParam</code> to [[SDL_iPhoneSetAnimationCallback]]().

This function is only available on Apple iOS.

For more information see:
https://github.com/libsdl-org/SDL/blob/main/docs/README-ios.md

This functions is also accessible using the macro
[[SDL_iOSSetAnimationCallback]]() since SDL 2.0.4.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_iPhoneSetEventPump]]

----
[[CategoryAPI]]


