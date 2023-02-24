====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetRenderMetalLayer =

Get the CAMetalLayer associated with the given Metal renderer.

== Syntax ==

<syntaxhighlight lang='c'>
void* SDL_GetRenderMetalLayer(SDL_Renderer *renderer);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|The renderer to query
|}

== Return Value ==

Returns a <code>CAMetalLayer *</code> on success, or NULL if the renderer
isn't a Metal renderer

== Remarks ==

This function returns <code>void *</code>, so SDL doesn't have to include
Metal's headers, but it can be safely cast to a <code>CAMetalLayer
*</code>.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetRenderMetalCommandEncoder]]

----
[[CategoryAPI]]


