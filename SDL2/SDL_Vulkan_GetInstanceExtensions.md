====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_Vulkan_GetInstanceExtensions =

Get the names of the Vulkan instance extensions needed to create a surface with [[SDL_Vulkan_CreateSurface]].

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_Vulkan_GetInstanceExtensions(SDL_Window *window,
                                          unsigned int *pCount,
                                          const char **pNames);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|A window for which the required Vulkan instance extensions should be retrieved (will be deprecated in a future release)
|-
|'''pCount'''
|A pointer to an unsigned int corresponding to the number of extensions to be returned
|-
|'''pNames'''
|NULL or a pointer to an array to be filled with required Vulkan instance extensions
|}

== Return Value ==

Returns [[SDL_TRUE]] on success, [[SDL_FALSE]] on error.

== Remarks ==

If <code>pNames</code> is NULL, then the number of required Vulkan instance
extensions is returned in <code>pCount</code>. Otherwise,
<code>pCount</code> must point to a variable set to the number of elements
in the <code>pNames</code> array, and on return the variable is overwritten
with the number of names actually written to <code>pNames</code>. If
<code>pCount</code> is less than the number of required extensions, at most
<code>pCount</code> structures will be written. If <code>pCount</code> is
smaller than the number of required extensions, [[SDL_FALSE]] will be
returned instead of [[SDL_TRUE]], to indicate that not all the required
extensions were returned.

The <code>window</code> parameter is currently needed to be valid as of SDL
2.0.8, however, this parameter will likely be removed in future releases

== Version ==

This function is available since SDL 2.0.6.

== Related Functions ==

:[[SDL_Vulkan_CreateSurface]]

----
[[CategoryAPI]]


