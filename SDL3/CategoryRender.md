# 2D Accelerated Rendering

'''Include File(s):''' [https://github.com/libsdl-org/SDL/blob/main/include/SDL_render.h SDL_render.h]


## Introduction
This category contains functions for 2D accelerated rendering.

This API supports the following features:

* single pixel points
* single pixel lines
* filled rectangles
* texture images

All of these may be drawn in opaque, blended, or additive modes.

The texture images can have an additional color tint or alpha modulation applied to them, and may also be stretched with linear interpolation, rotated or flipped/mirrored.

For advanced functionality like particle effects or actual 3D you should use SDL's OpenGL/Direct3D support or one of the many available 3D engines.

This API is not designed to be used from multiple threads, see [https://github.com/libsdl-org/SDL/issues/986 SDL issue #986] for details.

<!-- BEGIN CATEGORY LIST -->
- [SDL_BlendFactor](SDL_BlendFactor)
- [SDL_BlendOperation](SDL_BlendOperation)
- [SDL_GetRenderDriverInfo](SDL_GetRenderDriverInfo)
- [SDL_GetRendererOutputSize](SDL_GetRendererOutputSize)
- [SDL_RenderCopy](SDL_RenderCopy)
- [SDL_RenderCopyEx](SDL_RenderCopyEx)
- [SDL_RenderDrawLine](SDL_RenderDrawLine)
- [SDL_RenderDrawLines](SDL_RenderDrawLines)
- [SDL_RenderDrawPoint](SDL_RenderDrawPoint)
- [SDL_RenderDrawPoints](SDL_RenderDrawPoints)
- [SDL_RenderDrawRect](SDL_RenderDrawRect)
- [SDL_RenderDrawRects](SDL_RenderDrawRects)
- [SDL_Renderer](SDL_Renderer)
- [SDL_RendererFlags](SDL_RendererFlags)
- [SDL_RendererFlip](SDL_RendererFlip)
- [SDL_RendererInfo](SDL_RendererInfo)
- [SDL_RenderTargetSupported](SDL_RenderTargetSupported)
- [SDL_Texture](SDL_Texture)
- [SDL_TextureAccess](SDL_TextureAccess)
- [SDL_TextureModulate](SDL_TextureModulate)
<!-- END CATEGORY LIST -->

----
[[CategoryCategory]]
