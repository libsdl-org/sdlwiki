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
* [[SDL_BlendFactor]]
* [[SDL_BlendOperation]]
* [[SDL_ComposeCustomBlendMode]]
* [[SDL_CreateRenderer]]
* [[SDL_CreateSoftwareRenderer]]
* [[SDL_CreateTexture]]
* [[SDL_CreateTextureFromSurface]]
* [[SDL_CreateWindowAndRenderer]]
* [[SDL_DestroyRenderer]]
* [[SDL_DestroyTexture]]
* [[SDL_GetNumRenderDrivers]]
* [[SDL_GetRenderDrawBlendMode]]
* [[SDL_GetRenderDrawColor]]
* [[SDL_GetRenderDriverInfo]]
* [[SDL_GetRenderer]]
* [[SDL_GetRendererInfo]]
* [[SDL_GetRendererOutputSize]]
* [[SDL_GetRenderTarget]]
* [[SDL_GetTextureAlphaMod]]
* [[SDL_GetTextureBlendMode]]
* [[SDL_GetTextureColorMod]]
* [[SDL_GL_BindTexture]]
* [[SDL_GL_UnbindTexture]]
* [[SDL_LockTexture]]
* [[SDL_QueryTexture]]
* [[SDL_RenderClear]]
* [[SDL_RenderCopy]]
* [[SDL_RenderCopyEx]]
* [[SDL_RenderDrawLine]]
* [[SDL_RenderDrawLines]]
* [[SDL_RenderDrawPoint]]
* [[SDL_RenderDrawPoints]]
* [[SDL_RenderDrawRect]]
* [[SDL_RenderDrawRects]]
* [[SDL_Renderer]]
* [[SDL_RendererFlags]]
* [[SDL_RendererFlip]]
* [[SDL_RendererInfo]]
* [[SDL_RenderFillRect]]
* [[SDL_RenderFillRects]]
* [[SDL_RenderGeometry]]
* [[SDL_RenderGeometryRaw]]
* [[SDL_RenderPresent]]
* [[SDL_RenderReadPixels]]
* [[SDL_RenderTargetSupported]]
* [[SDL_SetRenderDrawBlendMode]]
* [[SDL_SetRenderDrawColor]]
* [[SDL_SetRenderTarget]]
* [[SDL_SetTextureAlphaMod]]
* [[SDL_SetTextureBlendMode]]
* [[SDL_SetTextureColorMod]]
* [[SDL_Texture]]
* [[SDL_TextureAccess]]
* [[SDL_TextureModulate]]
* [[SDL_UnlockTexture]]
* [[SDL_UpdateTexture]]
* [[SDL_UpdateYUVTexture]]
<!-- END CATEGORY LIST -->

----
[[CategoryCategory]]
