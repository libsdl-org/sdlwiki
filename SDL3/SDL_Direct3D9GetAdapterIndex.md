====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
= SDL_Direct3D9GetAdapterIndex =

Get the D3D9 adapter index that matches the specified display.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_Direct3D9GetAdapterIndex(SDL_DisplayID displayID);
</syntaxhighlight>

== Function Parameters ==

{|
|'''displayID'''
|the instance of the display to query
|}

== Return Value ==

Returns the D3D9 adapter index on success or a negative error code on
failure; call [[SDL_GetError]]() for more information.

== Remarks ==

The returned adapter index can be passed to
<code>IDirect3D9::CreateDevice</code> and controls on which monitor a full
screen application will appear.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]], [[CategorySystem]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


