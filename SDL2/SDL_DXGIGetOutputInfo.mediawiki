====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_DXGIGetOutputInfo =

Get the DXGI Adapter and Output indices for the specified display index.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_DXGIGetOutputInfo( int displayIndex, int *adapterIndex, int *outputIndex );
</syntaxhighlight>

== Function Parameters ==

{|
|'''displayIndex'''
|the display index for which to get both indices
|-
|'''adapterIndex'''
|a pointer to be filled in with the adapter index
|-
|'''outputIndex'''
|a pointer to be filled in with the output index
|}

== Return Value ==

Returns [[SDL_TRUE]] on success or [[SDL_FALSE]] on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

The DXGI Adapter and Output indices can be passed to
<code>EnumAdapters</code> and <code>EnumOutputs</code> respectively to get
the objects required to create a DX10 or DX11 device and swap chain.

Before SDL 2.0.4 this function did not return a value. Since SDL 2.0.4 it
returns an [[SDL_bool]].

== Version ==

This function is available since SDL 2.0.2.

----
[[CategoryAPI]]


