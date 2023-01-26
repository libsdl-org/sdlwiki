====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderGetD3D9Device =

Get the D3D9 device associated with a renderer.

== Syntax ==

<syntaxhighlight lang='c'>
IDirect3DDevice9* SDL_RenderGetD3D9Device(SDL_Renderer * renderer);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the renderer from which to get the associated D3D device
|}

== Return Value ==

Returns the D3D9 device associated with given renderer or NULL if it is not
a D3D9 renderer; call [[SDL_GetError]]() for more information.

== Remarks ==

Once you are done using the device, you should release it to avoid a
resource leak.

== Version ==

This function is available since SDL 2.0.1.

----
[[CategoryAPI]]


