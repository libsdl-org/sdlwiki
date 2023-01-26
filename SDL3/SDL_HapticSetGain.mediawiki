====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!
= SDL_HapticSetGain =

Set the global gain of the specified haptic device.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticSetGain(SDL_Haptic * haptic, int gain);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to set the gain on
|-
|'''gain'''
|value to set the gain to, should be between 0 and 100 (0 - 100)
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

Device must support the [[SDL_HAPTIC_GAIN]] feature.

The user may specify the maximum gain by setting the environment variable
<code>[[SDL_HAPTIC_GAIN_MAX]]</code> which should be between 0 and 100. All
calls to [[SDL_HapticSetGain]]() will scale linearly using
<code>[[SDL_HAPTIC_GAIN_MAX]]</code> as the maximum.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_HapticQuery]]

----
[[CategoryAPI]], [[CategoryForceFeedback]], [[CategoryDraft]]


