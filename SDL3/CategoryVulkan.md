# Vulkan Support


'''Include File(s):''' [http://hg.libsdl.org/SDL/file/default/include/SDL_vulkan.h SDL_vulkan.h]




## Introduction

This category contains functions for creating a Vulkan instance with the required Vulkan extensions for surface creation.

The general flow of a Vulkan backed SDL application will be the following:

# Create your SDL window with the SDL_WINDOW_VULKAN flag.
# If necessary, use [[SDL_Vulkan_LoadLibrary]] and [[SDL_Vulkan_GetVkInstanceProcAddr]] to load the Vulkan library and query for driver function pointers (after initializing the video subsystem)
# Query for required extensions using [[SDL_Vulkan_GetInstanceExtensions]] and use this information to create a ```VkInstance```
# Create a surface for the window to draw on using [[SDL_Vulkan_CreateSurface]]
# When setting up pipelines and framebuffers for your newly created surface, use [[SDL_Vulkan_GetDrawableSize]] to query the surface extent

## Functions

<!-- BEGIN CATEGORY LIST -->
* [[SDL_Vulkan_CreateSurface]]
* [[SDL_Vulkan_GetDrawableSize]]
* [[SDL_Vulkan_GetInstanceExtensions]]
* [[SDL_Vulkan_GetVkInstanceProcAddr]]
* [[SDL_Vulkan_LoadLibrary]]
* [[SDL_Vulkan_UnloadLibrary]]
<!-- END CATEGORY LIST -->

----
[[CategoryCategory]]
