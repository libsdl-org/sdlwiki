====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!
= SDL_HapticSetAutocenter =

Set the global autocenter of the device.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticSetAutocenter(SDL_Haptic * haptic,
                            int autocenter);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to set autocentering on
|-
|'''autocenter'''
|value to set autocenter to (0-100)
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

Autocenter should be between 0 and 100. Setting it to 0 will disable
autocentering.

Device must support the [[SDL_HAPTIC_AUTOCENTER]] feature.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_HapticQuery]]

----
[[CategoryAPI]], [[CategoryForceFeedback]], [[CategoryDraft]]


