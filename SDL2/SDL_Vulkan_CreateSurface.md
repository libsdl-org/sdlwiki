====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_Vulkan_CreateSurface =

Create a Vulkan rendering surface for a window.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_Vulkan_CreateSurface(SDL_Window *window,
                                  VkInstance instance,
                                  VkSurfaceKHR* surface);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|The window to which to attach the Vulkan surface
|-
|'''instance'''
|The Vulkan instance handle
|-
|'''surface'''
|A pointer to a VkSurfaceKHR handle to output the newly created surface
|}

== Return Value ==

Returns [[SDL_TRUE]] on success, [[SDL_FALSE]] on error.

== Remarks ==

The <code>window</code> must have been created with the
<code>[[SDL_WINDOW_VULKAN]]</code> flag and <code>instance</code> must have
been created with extensions returned by
[[SDL_Vulkan_GetInstanceExtensions]]() enabled.

== Version ==

This function is available since SDL 2.0.6.

== Related Functions ==

:[[SDL_Vulkan_GetInstanceExtensions]]
:[[SDL_Vulkan_GetDrawableSize]]

----
[[CategoryAPI]]


