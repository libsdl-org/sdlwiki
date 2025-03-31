# CategoryGPU

The GPU API offers a cross-platform way for apps to talk to modern graphics
hardware. It offers both 3D graphics and compute support, by utilizing the
Metal, Vulkan, or Direct3D 12 APIs.

A basic workflow might be something like this:

The app creates a GPU device with
[SDL_CreateGPUDevice](SDL_CreateGPUDevice)(), and assigns it to a window
with [SDL_ClaimWindowForGPUDevice](SDL_ClaimWindowForGPUDevice)()--although
strictly speaking you can render offscreen entirely, for things like image
processing, and not use a window at all.

Next, the app prepares static data (things that are created once and used
over and over). For example:

- Shaders (programs that run on the GPU): use
  [SDL_CreateGPUShader](SDL_CreateGPUShader)().
- Vertex buffers (arrays of geometry data) and other rendering data: use
  [SDL_CreateGPUBuffer](SDL_CreateGPUBuffer)() and
  [SDL_UploadToGPUBuffer](SDL_UploadToGPUBuffer)().
- Textures (images): use [SDL_CreateGPUTexture](SDL_CreateGPUTexture)() and
  [SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)().
- Samplers (how textures should be read from): use
  [SDL_CreateGPUSampler](SDL_CreateGPUSampler)().
- Render pipelines (precalculated rendering state): use
  [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)()

To render, the app creates one or more command buffer, with
[SDL_AcquireGPUCommandBuffer](SDL_AcquireGPUCommandBuffer)(). Command
buffers collect rendering instructions that will be submitted to the GPU in batches. Complex scenes can use multiple command buffers, configured
across multiple threads in parallel or just on the main thread, as long as they are submitted in the
correct order, but most apps will just need one command buffer per frame.

Rendering is applied to a texture (what other APIs call a "render target")
or it can be done to a swapchain texture (which is just a special texture
that represents a window's contents). The app can use
[SDL_WaitAndAcquireGPUSwapchainTexture](SDL_WaitAndAcquireGPUSwapchainTexture)()
to render to the window.

Rendering actually happens in a Render Pass, which is encoded into a
command buffer. One can encode multiple render passes (or alternate between
render and compute passes) in a single command buffer, but most apps 
simply need a single render pass for a single command buffer. Render Passes
can render to up to four color textures and one depth texture
simultaneously. If the textures being rendered need to change,
the Render Pass must be ended and a new one must be begun.

The app calls [SDL_BeginGPURenderPass](SDL_BeginGPURenderPass)(). Then it
sets states it needs for each draw:

- [SDL_BindGPUGraphicsPipeline](SDL_BindGPUGraphicsPipeline)()
- [SDL_SetGPUViewport](SDL_SetGPUViewport)()
- [SDL_BindGPUVertexBuffers](SDL_BindGPUVertexBuffers)()
- [SDL_BindGPUVertexSamplers](SDL_BindGPUVertexSamplers)()
- etc

Then, make the actual draw commands with these states:

- [SDL_DrawGPUPrimitives](SDL_DrawGPUPrimitives)()
- [SDL_DrawGPUPrimitivesIndirect](SDL_DrawGPUPrimitivesIndirect)()
- [SDL_DrawGPUIndexedPrimitivesIndirect](SDL_DrawGPUIndexedPrimitivesIndirect)()
- etc

After all the drawing commands for a pass are complete, the app should call
[SDL_EndGPURenderPass](SDL_EndGPURenderPass)(). Once a render pass ends all
render-related states are reset.

The app can begin new Render Passes and make new draws in the same command
buffer until the entire scene is rendered.

Once all of the render commands for the scene are complete, the app calls
[SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)() to send it to
the GPU for processing.

If the app needs to read back data from texture or buffers, the API has an
efficient way of doing this, provided that the app is willing to tolerate
some latency. When the app uses
[SDL_DownloadFromGPUTexture](SDL_DownloadFromGPUTexture)() or
[SDL_DownloadFromGPUBuffer](SDL_DownloadFromGPUBuffer)(), submitting the
command buffer with
[SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)()
will return a fence handle that the app can poll or wait on in a thread.
Once the fence indicates that the command buffer is done processing, it is
safe to read the downloaded data. Make sure to call
[SDL_ReleaseGPUFence](SDL_ReleaseGPUFence)() when done with the fence.

The API also has "compute" support. The app calls
[SDL_BeginGPUComputePass](SDL_BeginGPUComputePass)() with compute-writeable
textures and/or buffers, which can be written to in a compute shader. Then
it sets states it needs for the compute dispatches:

- [SDL_BindGPUComputePipeline](SDL_BindGPUComputePipeline)()
- [SDL_BindGPUComputeStorageBuffers](SDL_BindGPUComputeStorageBuffers)()
- [SDL_BindGPUComputeStorageTextures](SDL_BindGPUComputeStorageTextures)()

Then, dispatch compute work:

- [SDL_DispatchGPUCompute](SDL_DispatchGPUCompute)()

For advanced users, this opens up powerful GPU-driven workflows.

Graphics and compute pipelines require the use of shaders, which as
mentioned above are small programs executed on the GPU. Each backend
(Vulkan, Metal, D3D12) requires a different shader format. When the app
creates the GPU device, the app lets the device know which shader formats
the app can provide. It will then select the appropriate backend depending
on the available shader formats and the backends available on the platform.
When creating shaders, the app must provide the correct shader format for
the selected backend. If you would like to learn more about why the API
works this way, there is a detailed
[blog post](https://moonside.games/posts/layers-all-the-way-down/)
explaining this situation.

It is optimal for apps to pre-compile the shader formats they might use,
but for ease of use SDL provides a separate project,
[[SDL_shadercross](SDL_shadercross)](https://github.com/libsdl-org/SDL_shadercross)
, for performing runtime shader cross-compilation. It also has a CLI
interface for offline precompilation as well.

This is an extremely quick overview that leaves out several important
details. Already, though, one can see that GPU programming can be quite
complex! If you just need simple 2D graphics, the
[Render API](https://wiki.libsdl.org/SDL3/CategoryRender)
is much easier to use but still hardware-accelerated. That said, even for
2D applications the performance benefits and expressiveness of the GPU API
are significant.

The GPU API targets a feature set with a wide range of hardware support and
ease of portability. It is designed so that the app won't have to branch
itself by querying feature support. If you need cutting-edge features with
limited hardware support, this API is probably not for you.

Examples demonstrating proper usage of this API can be found
[here](https://github.com/TheSpydog/SDL_gpu_examples)
.

## Performance considerations

Here are some basic tips for maximizing your rendering performance.

- Beginning a new render pass is relatively expensive. Use as few render
  passes as you can.
- Minimize the amount of state changes. For example, binding a pipeline is
  relatively cheap, but doing it hundreds of times when you don't need to
  will slow the performance significantly.
- Perform your data uploads as early as possible in the frame.
- Don't churn resources. Creating and releasing resources is expensive.
  It's better to create what you need up front and cache it.
- Don't use uniform buffers for large amounts of data (more than a matrix
  or so). Use a storage buffer instead.
- Use cycling correctly. There is a detailed explanation of cycling further
  below.
- Use culling techniques to minimize pixel writes. The less writing the GPU
  has to do the better. Culling can be a very advanced topic but even
  simple culling techniques can boost performance significantly.

In general try to remember the golden rule of performance: doing things is
more expensive than not doing things. Don't Touch The Driver!

## FAQ

**Question: When are you adding more advanced features, like ray tracing or
mesh shaders?**

Answer: We don't have immediate plans to add more bleeding-edge features,
but we certainly might in the future, when these features prove worthwhile,
and reasonable to implement across several platforms and underlying APIs.
So while these things are not in the "never" category, they are definitely
not "near future" items either.

**Question: Why is my shader not working?**

Answer: A common oversight when using shaders is not properly laying out
the shader resources/registers correctly. The GPU API is very strict with
how it wants resources to be laid out and it's difficult for the API to
automatically validate shaders to see if they have a compatible layout. See
the documentation for [SDL_CreateGPUShader](SDL_CreateGPUShader)() and
[SDL_CreateGPUComputePipeline](SDL_CreateGPUComputePipeline)() for
information on the expected layout.

Another common issue is not setting the correct number of samplers,
textures, and buffers in
[SDL_GPUShaderCreateInfo](SDL_GPUShaderCreateInfo). If possible use shader
reflection to extract the required information from the shader
automatically instead of manually filling in the struct's values.

**Question: My application isn't performing very well. Is this the GPU
API's fault?**

Answer: No. Long answer: The GPU API is a relatively thin layer over the
underlying graphics API. While it's possible that we have done something
inefficiently, it's very unlikely especially if you are relatively
inexperienced with GPU rendering. Please see the performance tips above and
make sure you are following them. Additionally, tools like RenderDoc can be
very helpful for diagnosing incorrect behavior and performance issues.

## System Requirements

**Vulkan:** Supported on Windows, Linux, Nintendo Switch, and certain
Android devices. Requires Vulkan 1.0 with the following extensions and
device features:

- `VK_KHR_swapchain`
- `VK_KHR_maintenance1`
- `independentBlend`
- `imageCubeArray`
- `depthClamp`
- `shaderClipDistance`
- `drawIndirectFirstInstance`
- `sampleRateShading`

**D3D12:** Supported on Windows 10 or newer, Xbox One (GDK), and Xbox
Series X|S (GDK). Requires a GPU that supports DirectX 12 Feature Level
11_1.

**Metal:** Supported on macOS 10.14+ and iOS/tvOS 13.0+. Hardware
requirements vary by operating system:

- macOS requires an Apple Silicon or
  [Intel Mac2 family](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_macos_gpufamily2_v1?language=objc)
  GPU
- iOS/tvOS requires an A9 GPU or newer
- iOS Simulator and tvOS Simulator are unsupported

## Uniform Data

Uniforms are for passing data to shaders. The uniform data will be constant
across all executions of the shader.

There are 4 available uniform slots per shader stage (where the stages are
vertex, fragment, and compute). Uniform data pushed to a slot on a stage
keeps its value throughout the command buffer until you call the relevant
Push function on that slot again.

For example, you could write your vertex shaders to read a camera matrix
from uniform binding slot 0, push the camera matrix at the start of the
command buffer, and that data will be used for every subsequent draw call.

It is valid to push uniform data during a render or compute pass.

Uniforms are best for pushing small amounts of data. If you are pushing
more than a matrix or two per call you should consider using a storage
buffer instead.

## A Note On Cycling

When using a command buffer, operations do not occur immediately - they
occur some time after the command buffer is submitted.

When a resource is used in a pending or active command buffer, it is
considered to be "bound". When a resource is no longer used in any pending
or active command buffers, it is considered to be "unbound".

If data resources are bound, it is unspecified when that data will be
unbound unless you acquire a fence when submitting the command buffer and
wait on it. However, this doesn't mean you need to track resource usage
manually.

All of the functions and structs that involve writing to a resource have a
"cycle" bool. [SDL_GPUTransferBuffer](SDL_GPUTransferBuffer),
[SDL_GPUBuffer](SDL_GPUBuffer), and [SDL_GPUTexture](SDL_GPUTexture) all
effectively function as ring buffers on internal resources. When cycle is
true, if the resource is bound, the cycle rotates to the next unbound
internal resource, or if none are available, a new one is created. This
means you don't have to worry about complex state tracking and
synchronization as long as cycling is correctly employed.

For example: you can call
[SDL_MapGPUTransferBuffer](SDL_MapGPUTransferBuffer)(), write texture data,
[SDL_UnmapGPUTransferBuffer](SDL_UnmapGPUTransferBuffer)(), and then
[SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)(). The next time you write
texture data to the transfer buffer, if you set the cycle param to true,
you don't have to worry about overwriting any data that is not yet
uploaded.

Another example: If you are using a texture in a render pass every frame,
this can cause a data dependency between frames. If you set cycle to true
in the [SDL_GPUColorTargetInfo](SDL_GPUColorTargetInfo) struct, you can
prevent this data dependency.

Cycling will never undefine already bound data. When cycling, all data in
the resource is considered to be undefined for subsequent commands until
that data is written again. You must take care not to read undefined data.

Note that when cycling a texture, the entire texture will be cycled, even
if only part of the texture is used in the call, so you must consider the
entire texture to contain undefined data after cycling.

You must also take care not to overwrite a section of data that has been
referenced in a command without cycling first. It is OK to overwrite
unreferenced data in a bound resource without cycling, but overwriting a
section of data that has already been referenced will produce unexpected
results.

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryGPU, CategoryAPIFunction -->
- [SDL_AcquireGPUCommandBuffer](SDL_AcquireGPUCommandBuffer)
- [SDL_AcquireGPUSwapchainTexture](SDL_AcquireGPUSwapchainTexture)
- [SDL_BeginGPUComputePass](SDL_BeginGPUComputePass)
- [SDL_BeginGPUCopyPass](SDL_BeginGPUCopyPass)
- [SDL_BeginGPURenderPass](SDL_BeginGPURenderPass)
- [SDL_BindGPUComputePipeline](SDL_BindGPUComputePipeline)
- [SDL_BindGPUComputeSamplers](SDL_BindGPUComputeSamplers)
- [SDL_BindGPUComputeStorageBuffers](SDL_BindGPUComputeStorageBuffers)
- [SDL_BindGPUComputeStorageTextures](SDL_BindGPUComputeStorageTextures)
- [SDL_BindGPUFragmentSamplers](SDL_BindGPUFragmentSamplers)
- [SDL_BindGPUFragmentStorageBuffers](SDL_BindGPUFragmentStorageBuffers)
- [SDL_BindGPUFragmentStorageTextures](SDL_BindGPUFragmentStorageTextures)
- [SDL_BindGPUGraphicsPipeline](SDL_BindGPUGraphicsPipeline)
- [SDL_BindGPUIndexBuffer](SDL_BindGPUIndexBuffer)
- [SDL_BindGPUVertexBuffers](SDL_BindGPUVertexBuffers)
- [SDL_BindGPUVertexSamplers](SDL_BindGPUVertexSamplers)
- [SDL_BindGPUVertexStorageBuffers](SDL_BindGPUVertexStorageBuffers)
- [SDL_BindGPUVertexStorageTextures](SDL_BindGPUVertexStorageTextures)
- [SDL_BlitGPUTexture](SDL_BlitGPUTexture)
- [SDL_CalculateGPUTextureFormatSize](SDL_CalculateGPUTextureFormatSize)
- [SDL_CancelGPUCommandBuffer](SDL_CancelGPUCommandBuffer)
- [SDL_ClaimWindowForGPUDevice](SDL_ClaimWindowForGPUDevice)
- [SDL_CopyGPUBufferToBuffer](SDL_CopyGPUBufferToBuffer)
- [SDL_CopyGPUTextureToTexture](SDL_CopyGPUTextureToTexture)
- [SDL_CreateGPUBuffer](SDL_CreateGPUBuffer)
- [SDL_CreateGPUComputePipeline](SDL_CreateGPUComputePipeline)
- [SDL_CreateGPUDevice](SDL_CreateGPUDevice)
- [SDL_CreateGPUDeviceWithProperties](SDL_CreateGPUDeviceWithProperties)
- [SDL_CreateGPUGraphicsPipeline](SDL_CreateGPUGraphicsPipeline)
- [SDL_CreateGPUSampler](SDL_CreateGPUSampler)
- [SDL_CreateGPUShader](SDL_CreateGPUShader)
- [SDL_CreateGPUTexture](SDL_CreateGPUTexture)
- [SDL_CreateGPUTransferBuffer](SDL_CreateGPUTransferBuffer)
- [SDL_DestroyGPUDevice](SDL_DestroyGPUDevice)
- [SDL_DispatchGPUCompute](SDL_DispatchGPUCompute)
- [SDL_DispatchGPUComputeIndirect](SDL_DispatchGPUComputeIndirect)
- [SDL_DownloadFromGPUBuffer](SDL_DownloadFromGPUBuffer)
- [SDL_DownloadFromGPUTexture](SDL_DownloadFromGPUTexture)
- [SDL_DrawGPUIndexedPrimitives](SDL_DrawGPUIndexedPrimitives)
- [SDL_DrawGPUIndexedPrimitivesIndirect](SDL_DrawGPUIndexedPrimitivesIndirect)
- [SDL_DrawGPUPrimitives](SDL_DrawGPUPrimitives)
- [SDL_DrawGPUPrimitivesIndirect](SDL_DrawGPUPrimitivesIndirect)
- [SDL_EndGPUComputePass](SDL_EndGPUComputePass)
- [SDL_EndGPUCopyPass](SDL_EndGPUCopyPass)
- [SDL_EndGPURenderPass](SDL_EndGPURenderPass)
- [SDL_GDKResumeGPU](SDL_GDKResumeGPU)
- [SDL_GDKSuspendGPU](SDL_GDKSuspendGPU)
- [SDL_GenerateMipmapsForGPUTexture](SDL_GenerateMipmapsForGPUTexture)
- [SDL_GetGPUDeviceDriver](SDL_GetGPUDeviceDriver)
- [SDL_GetGPUDriver](SDL_GetGPUDriver)
- [SDL_GetGPUShaderFormats](SDL_GetGPUShaderFormats)
- [SDL_GetGPUSwapchainTextureFormat](SDL_GetGPUSwapchainTextureFormat)
- [SDL_GetNumGPUDrivers](SDL_GetNumGPUDrivers)
- [SDL_GPUSupportsProperties](SDL_GPUSupportsProperties)
- [SDL_GPUSupportsShaderFormats](SDL_GPUSupportsShaderFormats)
- [SDL_GPUTextureFormatTexelBlockSize](SDL_GPUTextureFormatTexelBlockSize)
- [SDL_GPUTextureSupportsFormat](SDL_GPUTextureSupportsFormat)
- [SDL_GPUTextureSupportsSampleCount](SDL_GPUTextureSupportsSampleCount)
- [SDL_InsertGPUDebugLabel](SDL_InsertGPUDebugLabel)
- [SDL_MapGPUTransferBuffer](SDL_MapGPUTransferBuffer)
- [SDL_PopGPUDebugGroup](SDL_PopGPUDebugGroup)
- [SDL_PushGPUComputeUniformData](SDL_PushGPUComputeUniformData)
- [SDL_PushGPUDebugGroup](SDL_PushGPUDebugGroup)
- [SDL_PushGPUFragmentUniformData](SDL_PushGPUFragmentUniformData)
- [SDL_PushGPUVertexUniformData](SDL_PushGPUVertexUniformData)
- [SDL_QueryGPUFence](SDL_QueryGPUFence)
- [SDL_ReleaseGPUBuffer](SDL_ReleaseGPUBuffer)
- [SDL_ReleaseGPUComputePipeline](SDL_ReleaseGPUComputePipeline)
- [SDL_ReleaseGPUFence](SDL_ReleaseGPUFence)
- [SDL_ReleaseGPUGraphicsPipeline](SDL_ReleaseGPUGraphicsPipeline)
- [SDL_ReleaseGPUSampler](SDL_ReleaseGPUSampler)
- [SDL_ReleaseGPUShader](SDL_ReleaseGPUShader)
- [SDL_ReleaseGPUTexture](SDL_ReleaseGPUTexture)
- [SDL_ReleaseGPUTransferBuffer](SDL_ReleaseGPUTransferBuffer)
- [SDL_ReleaseWindowFromGPUDevice](SDL_ReleaseWindowFromGPUDevice)
- [SDL_SetGPUAllowedFramesInFlight](SDL_SetGPUAllowedFramesInFlight)
- [SDL_SetGPUBlendConstants](SDL_SetGPUBlendConstants)
- [SDL_SetGPUBufferName](SDL_SetGPUBufferName)
- [SDL_SetGPUScissor](SDL_SetGPUScissor)
- [SDL_SetGPUStencilReference](SDL_SetGPUStencilReference)
- [SDL_SetGPUSwapchainParameters](SDL_SetGPUSwapchainParameters)
- [SDL_SetGPUTextureName](SDL_SetGPUTextureName)
- [SDL_SetGPUViewport](SDL_SetGPUViewport)
- [SDL_SubmitGPUCommandBuffer](SDL_SubmitGPUCommandBuffer)
- [SDL_SubmitGPUCommandBufferAndAcquireFence](SDL_SubmitGPUCommandBufferAndAcquireFence)
- [SDL_UnmapGPUTransferBuffer](SDL_UnmapGPUTransferBuffer)
- [SDL_UploadToGPUBuffer](SDL_UploadToGPUBuffer)
- [SDL_UploadToGPUTexture](SDL_UploadToGPUTexture)
- [SDL_WaitAndAcquireGPUSwapchainTexture](SDL_WaitAndAcquireGPUSwapchainTexture)
- [SDL_WaitForGPUFences](SDL_WaitForGPUFences)
- [SDL_WaitForGPUIdle](SDL_WaitForGPUIdle)
- [SDL_WaitForGPUSwapchain](SDL_WaitForGPUSwapchain)
- [SDL_WindowSupportsGPUPresentMode](SDL_WindowSupportsGPUPresentMode)
- [SDL_WindowSupportsGPUSwapchainComposition](SDL_WindowSupportsGPUSwapchainComposition)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryGPU, CategoryAPIDatatype -->
- [SDL_GPUBuffer](SDL_GPUBuffer)
- [SDL_GPUBufferUsageFlags](SDL_GPUBufferUsageFlags)
- [SDL_GPUColorComponentFlags](SDL_GPUColorComponentFlags)
- [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer)
- [SDL_GPUComputePass](SDL_GPUComputePass)
- [SDL_GPUComputePipeline](SDL_GPUComputePipeline)
- [SDL_GPUCopyPass](SDL_GPUCopyPass)
- [SDL_GPUDevice](SDL_GPUDevice)
- [SDL_GPUFence](SDL_GPUFence)
- [SDL_GPUGraphicsPipeline](SDL_GPUGraphicsPipeline)
- [SDL_GPURenderPass](SDL_GPURenderPass)
- [SDL_GPUSampler](SDL_GPUSampler)
- [SDL_GPUShader](SDL_GPUShader)
- [SDL_GPUShaderFormat](SDL_GPUShaderFormat)
- [SDL_GPUTexture](SDL_GPUTexture)
- [SDL_GPUTextureUsageFlags](SDL_GPUTextureUsageFlags)
- [SDL_GPUTransferBuffer](SDL_GPUTransferBuffer)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryGPU, CategoryAPIStruct -->
- [SDL_GPUBlitInfo](SDL_GPUBlitInfo)
- [SDL_GPUBlitRegion](SDL_GPUBlitRegion)
- [SDL_GPUBufferBinding](SDL_GPUBufferBinding)
- [SDL_GPUBufferCreateInfo](SDL_GPUBufferCreateInfo)
- [SDL_GPUBufferLocation](SDL_GPUBufferLocation)
- [SDL_GPUBufferRegion](SDL_GPUBufferRegion)
- [SDL_GPUColorTargetBlendState](SDL_GPUColorTargetBlendState)
- [SDL_GPUColorTargetDescription](SDL_GPUColorTargetDescription)
- [SDL_GPUColorTargetInfo](SDL_GPUColorTargetInfo)
- [SDL_GPUComputePipelineCreateInfo](SDL_GPUComputePipelineCreateInfo)
- [SDL_GPUDepthStencilState](SDL_GPUDepthStencilState)
- [SDL_GPUDepthStencilTargetInfo](SDL_GPUDepthStencilTargetInfo)
- [SDL_GPUGraphicsPipelineCreateInfo](SDL_GPUGraphicsPipelineCreateInfo)
- [SDL_GPUGraphicsPipelineTargetInfo](SDL_GPUGraphicsPipelineTargetInfo)
- [SDL_GPUIndexedIndirectDrawCommand](SDL_GPUIndexedIndirectDrawCommand)
- [SDL_GPUIndirectDispatchCommand](SDL_GPUIndirectDispatchCommand)
- [SDL_GPUIndirectDrawCommand](SDL_GPUIndirectDrawCommand)
- [SDL_GPUMultisampleState](SDL_GPUMultisampleState)
- [SDL_GPURasterizerState](SDL_GPURasterizerState)
- [SDL_GPUSamplerCreateInfo](SDL_GPUSamplerCreateInfo)
- [SDL_GPUShaderCreateInfo](SDL_GPUShaderCreateInfo)
- [SDL_GPUStencilOpState](SDL_GPUStencilOpState)
- [SDL_GPUStorageBufferReadWriteBinding](SDL_GPUStorageBufferReadWriteBinding)
- [SDL_GPUStorageTextureReadWriteBinding](SDL_GPUStorageTextureReadWriteBinding)
- [SDL_GPUTextureCreateInfo](SDL_GPUTextureCreateInfo)
- [SDL_GPUTextureLocation](SDL_GPUTextureLocation)
- [SDL_GPUTextureRegion](SDL_GPUTextureRegion)
- [SDL_GPUTextureSamplerBinding](SDL_GPUTextureSamplerBinding)
- [SDL_GPUTextureTransferInfo](SDL_GPUTextureTransferInfo)
- [SDL_GPUTransferBufferCreateInfo](SDL_GPUTransferBufferCreateInfo)
- [SDL_GPUTransferBufferLocation](SDL_GPUTransferBufferLocation)
- [SDL_GPUVertexAttribute](SDL_GPUVertexAttribute)
- [SDL_GPUVertexBufferDescription](SDL_GPUVertexBufferDescription)
- [SDL_GPUVertexInputState](SDL_GPUVertexInputState)
- [SDL_GPUViewport](SDL_GPUViewport)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryGPU, CategoryAPIEnum -->
- [SDL_GPUBlendFactor](SDL_GPUBlendFactor)
- [SDL_GPUBlendOp](SDL_GPUBlendOp)
- [SDL_GPUCompareOp](SDL_GPUCompareOp)
- [SDL_GPUCubeMapFace](SDL_GPUCubeMapFace)
- [SDL_GPUCullMode](SDL_GPUCullMode)
- [SDL_GPUFillMode](SDL_GPUFillMode)
- [SDL_GPUFilter](SDL_GPUFilter)
- [SDL_GPUFrontFace](SDL_GPUFrontFace)
- [SDL_GPUIndexElementSize](SDL_GPUIndexElementSize)
- [SDL_GPULoadOp](SDL_GPULoadOp)
- [SDL_GPUPresentMode](SDL_GPUPresentMode)
- [SDL_GPUPrimitiveType](SDL_GPUPrimitiveType)
- [SDL_GPUSampleCount](SDL_GPUSampleCount)
- [SDL_GPUSamplerAddressMode](SDL_GPUSamplerAddressMode)
- [SDL_GPUSamplerMipmapMode](SDL_GPUSamplerMipmapMode)
- [SDL_GPUShaderStage](SDL_GPUShaderStage)
- [SDL_GPUStencilOp](SDL_GPUStencilOp)
- [SDL_GPUStoreOp](SDL_GPUStoreOp)
- [SDL_GPUSwapchainComposition](SDL_GPUSwapchainComposition)
- [SDL_GPUTextureFormat](SDL_GPUTextureFormat)
- [SDL_GPUTextureType](SDL_GPUTextureType)
- [SDL_GPUTransferBufferUsage](SDL_GPUTransferBufferUsage)
- [SDL_GPUVertexElementFormat](SDL_GPUVertexElementFormat)
- [SDL_GPUVertexInputRate](SDL_GPUVertexInputRate)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategoryGPU, CategoryAPIMacro -->
- (none.)
<!-- END CATEGORY LIST -->
[CategoryAPICategory](CategoryAPICategory)