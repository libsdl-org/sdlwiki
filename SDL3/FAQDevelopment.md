# Frequently Asked Questions

Check these out if your questions aren't directly about using the library as a developer.
|                               |                                             |
| ----------------------------- | --------------------------------------------|
| [General](FAQGeneral)         | General questions about SDL                 |
| [Using SDL](FAQUsingSDL)      | Questions for people using SDL applications |
| [Licensing](FAQLicensing)     | Questions about licensing SDL with products |

## Table of contents

- [How do I do X? Is Y broken? (I couldn't find it on this page!)](#cant_find_answer)
- [Do I `#include <SDL.h>` or `#include <SDL3/SDL.h>`?](#include)
- [How do I load images, sounds, show UI, etc?](#asset_loading_and_ui)
- [Can I call SDL video functions from multiple threads?](#video_on_threads)
- [Can I call SDL event functions from multiple threads?](#events_on_threads)
- [Why is my sleep/SDL-Delay function inaccurate? (Why am I getting 61/62/59 fps and not 60?):](#inaccurate_sleep)
- [I'm getting an error about SDL_main, WinMain, main, etc:](#main)
- [Why is my window not rendering while the Window is being resized or dragged/moved?](#frozen_window)
- [Graphics](#graphics)
  - [Can I use shaders with the SDL 2D render API?](#renderer_shaders)
  - [What Graphics API Should I use?](#what_gpu_api)
  - [Can SDL_GPU run on OpenGL?](#gpu_on_gl)
  - [Can SDL_GPU run on Android? ](#gpu_on_android)
  - [What should I do for shaders for SDL_GPU or SDL_Renderer with the GPU backend?](#shader_choices)
  - [I'm trying to use SDL_shadercross as an online (runtime) compiler.](#shadercross_runtime)
  - [I'm on Linux and trying to run my SDL_GPU application under RenderDoc and don't get a Device, what's going on?](#renderdoc)


## How do I do X? Is Y broken? (I couldn't find it on this page!) <a name="cant_find_answer" id="cant_find_answer"></a>

If something isn't covered here, it doesn't mean we don't know about it! It's difficult to collate everything between bugs, intended but perhaps unexpected behavior, and even many Frequently Asked Questions.

When looking to do something, generally the first place to look is the [Category the API you're looking for is likely in](APIByCategory.md). If it has to do with a specific function, check the documentation for that, specifically the remarks section, there's fantastic information in those sections. If you still can't figure it out, SDL has several communities you can connect with to get help!

Regarding something seeming to be broken, you can first [search on the bug tracker](https://github.com/libsdl-org/SDL/issues). If you don't find anything but would like to check with other folks before reporting, you can drop by [one of the SDL related Communities](FAQCommunities.md)

## Do I `#include <SDL.h>` or `#include <SDL3/SDL.h>`? <a name="include" id="include"></a>

The most portable way to include SDL headers is to use angular quotes around the full header name:

```c
#include <SDL3/SDL.h>
```

This is new in SDL3! Previously, in SDL2, we recommended `#include "SDL.h"`, but this proved to be unfriendly to macOS frameworks and having the API version in the include line is useful for making dependency requirements clear.

## How do I load images, sounds, show UI, etc? <a name="asset_loading_and_ui" id="asset_loading_and_ui"></a>

SDL provides the lower level of functionality that a cross-platform game engine needs, leaving higher level tasks to other libraries. The [libraries page](Libraries) has a non-exhaustive list of libraries that are known to work well with SDL.

## Can I call SDL video functions from multiple threads? <a name="video_on_threads" id="video_on_threads"></a>

No, most graphics back ends are not thread-safe, so you should only call SDL video functions from the main thread of your application. [SDL_RunOnMainThread()](SDL_RunOnMainThread) can be used to dispatch code that needs to run on the main thread.

## Can I call SDL event functions from multiple threads? <a name="events_on_threads" id="events_on_threads"></a>

The main event handling should be done on the main thread, though you can use [SDL_PushEvent()](SDL_PushEvent) and [SDL_PeepEvents()](SDL_PeepEvents) to interact with the event queue on other threads. Most SDL functions have their thread-safety noted in their documentation.


## Why is my sleep/SDL-Delay function inaccurate? (Why am I getting 61/62/59 fps and not 60?): <a name="inaccurate_sleep" id="inaccurate_sleep"></a>

Take a look at these blogs for an in-depth understanding of the problems of timing:
 - https://blog.bearcats.nl/accurate-sleep-function/ (Recentlyish Updated)
 - https://blog.bearcats.nl/perfect-sleep-function/ (Part 2, even better Sleeps!)

In SDL3 you should be using [`SDL_DelayPrecise`](SDL_DelayPrecise)  (which uses an algorithm similar to above) or [`SDL_DelayNS`](SDL_DelayNS) (More precise than SDL_Delay, but doesn't busy-wait)

On a similar note, when doing timing, prefer using [`SDL_GetPerformanceCounter`](SDL_GetPerformanceCounter)  and [`SDL_GetPerformanceFrequency`](SDL_GetPerformanceFrequency) , or [`SDL_GetTicksNS`](SDL_GetTicksNS) , over using [`SDL_GetTicks`](SDL_GetTicks), which has only has millisecond precision. [`SDL_GetTicksNS`](SDL_GetTicksNS) uses [`SDL_GetPerformanceCounter`](SDL_GetPerformanceCounter) under the hood, but converted to nanoseconds for convenience.


## I'm getting an error about SDL_main, WinMain, main, etc: <a name="main" id="main"></a>

> NOTE: This answer is written for brevity, but this is a complex topic! For a full understanding of what's happening, please look over our [main functions README](README-main-functions).

It's _most_ likely you have `#include <SDL3/SDL_main.h>` included in the file with your `main` function, but your `main` function doesn't have the expected signature:
`int main(int argc, char *argv[])`

If you see an error about "a previous definition of `SDL_main`", there's pretty much two possibilities:
 - You've implemented `main` twice in one file yourself. Pretty unlikely, but it can happen!
 - More likely you have `#define SDL_MAIN_USE_CALLBACKS` somewhere, or have `SDL_MAIN_USE_CALLBACKS` defined through your build system as a switch to the compiler, but you're implementing `main` instead of or in addition to the callbacks.

The last common issue here is you've placed `#include "SDL3/SDL_main.h"` in two Translation Units (c/cpp files).

## Why is my window not rendering while the Window is being resized or dragged/moved? <a name="frozen_window" id="frozen_window"></a>

On some operating systems (notably Windows, but others as well), your call into [`SDL_PollEvent`](SDL_PollEvent), [`SDL_WaitEvent`](SDL_WaitEvent), [`SDL_WaitEventTimeout`](SDL_WaitEventTimeout), or [`SDL_PumpEvents`](SDL_PumpEvents) may block during resizing or dragging. This means these function will not return and yield control to your code, until the OS is done with this operation. That said, the OS's do provide ways for a user application to still do work during these operations, but they do so through callbacks, which is to say a function the user provides and the OS will call at appropriate times.

SDL provides two ways to get called during these blocking operations.
  - [The callbacks from `SDL_main.h`](README-main-functions#main-callbacks-in-sdl3)
    - Using this, `SDL_AppIterate` should be called for you, even when being resized or moved.
  - [SDL_SetEventFilter](SDL_SetEventFilter) (note though, that you cannot simply filter the event away and expect it to be unblocked) or [SDL_AddEventWatch](SDL_AddEventWatch)
    - Using one of these, you'll need to watch for the `SDL_EVENT_WINDOW_EXPOSED` event. That event will tell you you're blocked and to do whatever you need to do to keep your process healthy, including rerendering the Window so it doesn't stretch or look overly unnatural.

For further context, even when blocked the OS gives your application time slices during these operations, but they do so through callbacks themselves, not by returning back to user code. So the only solution is for SDL or similar to give you a callback as well.

There's also an asterisk in that there's still often some minor issues with this where a Window still may look imperfect during resizing. There are bugs open to hopefully figure this out and address it, that said, it's more of a perfectionist issue at this point.

Here's a program that demonstrates the callbacks still allowing user code to run during Window resize and move operations:

```c
#include <SDL3/SDL.h>

#define SDL_MAIN_USE_CALLBACKS
#include <SDL3/SDL_main.h>

SDL_Window* g_window;
SDL_Renderer* g_renderer;
SDL_FRect g_rect = {
    100.f, 100.f, 100.f, 100.f
};

SDL_AppResult SDL_AppInit(void** appstate, int argc, char** argv) {
    SDL_CreateWindowAndRenderer("Test", 300, 300, SDL_WINDOW_RESIZABLE, &g_window, &g_renderer);
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppIterate(void* appstate) {
    SDL_SetRenderDrawColor(g_renderer, 0, 0, 0, 255);
    SDL_RenderClear(g_renderer);

    SDL_FRect rect = g_rect;
    rect.x += 50 * SDL_sinf(SDL_GetTicksNS() / 1000000000.f);


    SDL_SetRenderDrawColor(g_renderer, 255, 255, 255, 255);
    SDL_RenderFillRect(g_renderer, &rect);


    SDL_RenderPresent(g_renderer);
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppEvent(void* appstate, SDL_Event* event) {
    if (event->common.type == SDL_EVENT_QUIT) {
        return SDL_APP_SUCCESS;
    }
    return SDL_APP_CONTINUE;
}

void SDL_AppQuit(void* appstate, SDL_AppResult result) { }
```

## Graphics <a name="graphics" id="graphics"></a>

### Can I use shaders with the SDL 2D render API?  <a name="renderer_shaders" id="renderer_shaders"></a>

No, unless you're using SDL 3.4 (as of yet unreleased). On SDL 3.4 you can get fragment shaders, take a look into [`SDL_CreateGPURenderState`](https://wiki.libsdl.org/SDL3/SDL_CreateGPURenderState).

That said, there are many different ways to use shaders, and if you need more than the subset of shader functionality we expose there, we recommend using a full 3D API like [SDL GPU](CategoryGPU). You can look at how SDL uses the GPU API for 2D rendering if you'd like to expand on that: [SDL_render_gpu.c](https://github.com/libsdl-org/SDL/blob/main/src/render/gpu/SDL_render_gpu.c)

### What Graphics API Should I use? <a name="what_gpu_api" id="what_gpu_api"></a>

This is a _very_ difficult question to give a good answer to. We'll try to give some soft recommendations here, along with information on the other native APIs so that you can decide for yourself what feels right for you.

We're quite proud of the new GPU api that was added in SDL3, and are confident it can handle the majority of use cases of users of SDL. FNA has already shipped games on console using SDL3 and the GPU api for rendering. That said, it's still early days of the API in terms of supplementary material. If you're intending to _learn_ graphics, we don't have a great story for ramping you up currently. In addition, while it has fairly wide platform support (note the big 3 console platforms), some important platforms are missing (Web) or degraded (Android). And if you need to target hardware more than about 10-13 years old, then you might be out of luck, there's not a ton of hardware DirectX12, Metal, or Vulkan support going that far back. And finally if you want newer features, like Work Groups, Mesh Shaders, Bindless Textures, then GPU won't be able to help there.

Now that we're through both positives and negatives of GPU, we'll try to give a rundown of some of the other options that might work for you.

- OpenGL and it's versions and variants
  - GL has it's problems, but if you're willing to put in the work, it's greatest strength is _wide_ platform support. Between desktop OpenGL and it's extensions, OpenGL ES, and WebGL, you can hit essentially every desktop going back 15 years or more, phones and various embedded devices, the web browser, and even the Nintendo Switch. It wouldn't be easy, you'd need to do a lot of version checking and changing depending on exactly which version and variant of GL you're targetting, but it is possible. 
  - GL also has some of the best learning resources, in particular [learnopengl.com](https://learnopengl.com/), a graphics tutorial and treatise so good that it's wildly common to suggest it for folks learning graphics on entirely different APIs.
  - The main downside is that by getting this wide platform support you're trading away both modern API design, and also modern APIs in general. Even targetting very new computers, it's likely you'd want to use the latest features in 4.6, which is unavailible on Macs.
- Vulkan
  - Vulkan is unfortunately most known for the "1000 line triangle", but if you're coming from something like OpenGL, it's explicitness might come as a breath of fresh air. It has decent platform support with Windows, MacOS and iOS(through MoltenVk), Linux, Android, and the Nintendo Switch. Although it should be noted that Vulkan shares the problems GPU has on Android, as it's the API that powers GPU on android. Newer versions reduce some of the boilerplate, and there are helpful libraries like [vma](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator) and [vk-bootstrap](https://github.com/charles-lunarg/vk-bootstrap) to help with some of the more tedious aspects of the API.
  - Vulkan tends to trail DirectX and Metal in new features, but it's still ahead of GPU, so if those features are important to you, it's well worth considering.
- DirectX12
  - If you're targetting only Windows 10 or 11, and the Xbox platform, DirectX might be worth considering. There's less boilerplate than Vulkan, but it's still quite explicit. It also tends to trade with Metal on bleeding edge features, but they're obviously mututally exclusive unless you're writing your own RHI (Render Hardware Interface) like GPU.
- Metal
  - The native API of Apples platforms, Graphics developers tend to be very happy with this API. It's got the least boilerplate of the 3 modern native APIs, tends to have excellent feature support and implementations, but is still very explicit so you're not leaving performance on the table.
  - The obvious main downside is it's only available on Apple platforms, and it can be somewhat difficult to use from languages besides Objective-C and Swift.

### Can SDL_GPU run on OpenGL? <a name="gpu_on_gl" id="gpu_on_gl"></a>

No, the backends are DX12, Metal, Vulkan. Although it should be noted that it's also supported on the NDA only console forks of SDL. (More information on how to get access on the [respective platform pages](README-platforms.md).)

### Can SDL_GPU run on Android?  <a name="gpu_on_android" id="gpu_on_android"></a>

Yes, but to get wide support, you'll need to give up on some features. Each Vulkan feature from the [properties you disable](SDL_CreateGPUDeviceWithProperties#remarks) when creating your [SDL_GPUDevice](SDL_GPUDevice) will get you wider Android support. In general if you're interested in Android you should just turn all of the Vulkan features here off. Hopefully in a year or two, things will improve as Google has announced somewhat agressive goals for upcoming Android versions.

### What should I do for shaders for SDL_GPU or SDL_Renderer with the GPU backend? <a name="shader_choices" id="shader_choices"></a>

We recommend using SDL_shadercross, a WIP shader compiler that tries to make it easy to go from HLSL to all the shader formats SDL_GPU needs for each backend. That said, we recommend not building it yourself, it 's still a bit temperamental. You can find builds on the [actions page](https://github.com/libsdl-org/SDL_shadercross/actions?query=branch%3Amain), just be signed into GitHub, and select the latest build from main.

### I'm trying to use SDL_shadercross as an online (runtime) compiler. <a name="shadercross_runtime" id="shadercross_runtime"></a>

Unfortunately there's not a lot of help we can provide here. If you're stepping outside of how the GitHub Actions builds things, you're bound to run into issues. There's some rather large and complicated dependencies underpinning SDL_shadercross and they complicate things significantly.

We hope to be able to update this answer in the near term with some better documentation around this!

### I'm on Linux and trying to run my SDL_GPU application under RenderDoc and don't get a Device, what's going on? <a name="renderdoc" id="renderdoc"></a>
It's likely that you're running Wayland. RenderDoc doesn't support Wayland, please force XWayland and give that a try!

You can set this before calling `SDL_Init` to get that behavior if your system is set up as expected:
`SDL_SetHint("SDL_HINT_VIDEO_DRIVER", "x11");`

