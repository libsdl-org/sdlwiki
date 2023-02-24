====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderGetD3D11Device =

Get the D3D11 device associated with a renderer.

== Syntax ==

<syntaxhighlight lang='c'>
ID3D11Device* SDL_RenderGetD3D11Device(SDL_Renderer * renderer);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the renderer from which to get the associated D3D11 device
|}

== Return Value ==

Returns the D3D11 device associated with given renderer or NULL if it is
not a D3D11 renderer; call [[SDL_GetError]]() for more information.

== Remarks ==

Once you are done using the device, you should release it to avoid a
resource leak.

== Version ==

This function is available since SDL 2.0.16.

----
[[CategoryAPI]]


