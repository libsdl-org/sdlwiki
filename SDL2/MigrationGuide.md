# SDL 1.2 to 2.0 Migration Guide


## Translations

- [Guía de migración a SDL 2.0](GuiaDeMigracion)
- Une traduction de cette page par Developpez.com est disponible [ici](http://jeux.developpez.com/tutoriels/sdl-2/guide-migration/).
- If you want to translate this page to other languages, just make a new page on the wiki and link to it here!

## Introduction

After many years in development, SDL 2.0 has finally been released!

We are quite proud of it, and we'd like games that are using SDL 1.2 to move up right away. As this can feel like a daunting task, this document is a simple walkthrough of how to migrate to the new library. We think you'll find it's not as hard as you think, and often times, you'll be either replacing function calls with direct equivalents or undoing some hacks in your code to deal with 1.2 deficiencies.

We think you'll be very happy with SDL 2.0, both for the new features and the better experience over SDL 1.2. This document doesn't try to cover all the awesome new things in SDL2--and there are many--but just the things you need to do to get running _right now_. Once you've ported your code, definitely check out the new stuff; you'll probably want to add some of it to your application, too.

### Overview of new features

These are the most important new features in SDL 2.0:

- Full 3D hardware acceleration
- Support for OpenGL 3.0+ in various profiles (core, compatibility, debug, robust, etc)
- Support for OpenGL ES
- Support for multiple windows
- Support for multiple displays
- Support for multiple audio devices
- Audio recording support
- Android and iOS support
- Emscripten and Native Client support
- Simple 2D rendering API that can use Direct3D, OpenGL, OpenGL ES, or software rendering behind the scenes
- Force Feedback
- XInput and XAudio2 support for Windows
- Atomic operations
- Power management (exposes battery life remaining, etc)
- Shaped windows
- 32-bit audio (int and float)
- Simplified Game Controller API (the Joystick API is still here, too!)
- Touch support (multitouch, gestures, etc)
- Better fullscreen support
- Better keyboard support (scancodes vs keycodes, etc).
- Message boxes
- Clipboard support
- APIs for building robust GUI toolkits on top of SDL
- Basic Drag'n'Drop support
- Proper unicode input and IME support
- [A really powerful assert macro](CategoryAssertions.md)
- zlib license instead of LGPL.
- Lots of old annoyances from 1.2 are gone
- Many other things!

The [Introduction](Introduction.md) page has a more extensive listing about what features SDL offers in overall (including old 1.2 features).

### Looking for more information

The best places for information are:

- this wiki :)
- the tests included in SDL, in the `test/` directory ([browse online](https://github.com/libsdl-org/SDL/tree/SDL2/test))
- the SDL [forums/mailing list](https://discourse.libsdl.org/)


## Moving from SDL 1.2 to 2.0

### Some general truths

There is no compatibility layer built in to SDL2. If an API changed for 2.0, we've changed or removed the old functions where it makes sense. If you point your 1.2 program at the 2.0 headers, it will probably fail to compile. This document will try to talk you through the most important changes, and the ones most likely to trip you up.

There's no SDL_main! Well, okay, there _is_, and it now does what it was always meant to: be a small piece of code that hides the difference between `main()` and `WinMain()` on Windows. There's no initialization code in it, and it's completely optional. This means you can use SDL without it taking over your mainline, which is nice for plugins that use SDL, or scripting languages with an SDL module. All the stuff you'd want the 1.2 `SDL_main` for is now in `SDL_Init()` where it belongs.

There's no SDL parachute anymore. What 1.2 called `SDL_INIT_NOPARACHUTE` is a default and only state now. This would cause problems if something other than the main thread crashed, and it would interfere with apps setting up their own signal/exception handlers. On the downside, some platforms don't clean up fullscreen video well when crashing. You should install your own crash handler, or call [SDL_Quit](SDL_Quit.md)() in an `atexit()` function or whatnot if this is a concern. Note that on Unix platforms, SDL still catches `SIGINT` and maps it to an [SDL_QUIT](SDL_EventType.md) event.


### Video

#### Setting up a game with the new video API

The video API is the most dramatic change from 1.2. Needs have changed a great deal since SDL's original API was designed in the late 1990's. To deal with modern hardware and OS features, we have almost completely replaced the old 1.2 video API.

Don't worry, the new one is pretty great, and once you understand what's changed, you're going to be very happy with the new features it can bring to your 1.2 game. We'll discuss those later.

The good news: if your game used OpenGL, you probably don't have much to do: change a handful of function calls to their SDL2 equivalents, and you're good to go.

For 2D graphics, SDL 1.2 offered a concept called "surfaces," which were memory buffers of pixels. The screen itself was a "surface," if you were doing 2D software rendering, and we provided functions to copy ("blit") pixels between surfaces, converting formats as necessary. You were almost always working on the CPU in system RAM, not on the GPU in video memory. SDL 2.0 changes this; you almost always get hardware acceleration now, and the API has changed to reflect this.

If you have a 2D game, chances are you've taken one of three approaches to rendering. We'll go through them all, but first, let's talk about introductory stuff.

Remember `SDL_SetVideoMode()`? It's completely gone. SDL 2.0 allows you to have multiple windows, so the old function didn't make sense any more.

So you might have had something like this:

```c
SDL_WM_SetCaption("My Game Window", "game");
SDL_Surface *screen = SDL_SetVideoMode(640, 480, 0, SDL_FULLSCREEN | SDL_OPENGL);
```

Which is now this:

```c
SDL_Window *screen = SDL_CreateWindow("My Game Window",
                          SDL_WINDOWPOS_UNDEFINED,
                          SDL_WINDOWPOS_UNDEFINED,
                          640, 480,
                          SDL_WINDOW_FULLSCREEN | SDL_WINDOW_OPENGL);
```

You can see that this maps pretty closely to 1.2. The difference is that you can have multiple windows (if you want), and you can control them more. `SDL_WM_SetCaption()` is gone, because we want to allow each window to have its own title (you can change it later with [SDL_SetWindowTitle](SDL_SetWindowTitle.md)()), and we want to let you specify a window position (or, in this case, use `SDL_WINDOWPOS_UNDEFINED` since we don't care where the system places it. `SDL_WINDOWPOS_CENTERED` is also a good choice).

Extra credit for letting users specify a display for the window: SDL2 also allows you to manage systems with multiple monitors. Don't worry about that right now, though.

So now that your window is back on the screen, let's talk strategy. SDL2 still has [[SDL_Surface]], but what you want, if possible, is the new [[SDL_Texture]]. Surfaces are always in system RAM now, and are always operated on by the CPU, so we want to get away from there. SDL2 has a new rendering API. It's meant for use by simple 2D games, but most notably, it's meant to get all that software rendering into video RAM and onto the GPU. And even if you just want to use it to get your software renderer's work to the screen, it brings some very nice benefits: if possible, it will use OpenGL or Direct3D behind the scenes, which means you'll get faster blits, a working Steam Overlay, and scaling for free.

The setup looks like this.

`SDL_SetVideoMode()` becomes [SDL_CreateWindow](SDL_CreateWindow.md)(), as we discussed before. But what do we put for the resolution? If your game was hardcoded to 640x480, for example, you probably were running into monitors that couldn't do that fullscreen resolution at this point, and in windowed mode, your game probably looked like an animated postage stamp on really high-end monitors. There's a better solution in SDL2.

We don't call `SDL_ListModes()` anymore. There's an equivalent in SDL2 (call [SDL_GetDisplayMode](SDL_GetDisplayMode.md)() in a loop, [SDL_GetNumDisplayModes](SDL_GetNumDisplayModes.md)() times), but instead we're going to use a new feature called "fullscreen desktop," which tells SDL "give me the whole screen and don't change the resolution." For our hypothetical 640x480 game, it might look like this:

```c
SDL_Window *sdlWindow = SDL_CreateWindow(title,
                             SDL_WINDOWPOS_UNDEFINED,
                             SDL_WINDOWPOS_UNDEFINED,
                             0, 0,
                             SDL_WINDOW_FULLSCREEN_DESKTOP);
```

Notice how we didn't specify 640 or 480...fullscreen desktop gives you the whole display and ignores any dimensions you specify. The game window should come up immediately, without waiting for the monitor to click into a new resolution, and we'll be using the GPU to scale to the desktop size, which tends to be faster and cleaner-looking than if an LCD is faking a lower resolution. Added bonus: none of your background windows are resizing themselves right now.

Now we need a rendering context.

```c
SDL_Renderer *renderer = SDL_CreateRenderer(sdlWindow, -1, 0);
```

A renderer hides the details of how we draw into the window. This might be using Direct3D, OpenGL, OpenGL ES, or software surfaces behind the scenes, depending on what the system offers; your code doesn't change, regardless of what SDL chooses (although you _are_ welcome to force one kind of renderer or another). If you want to attempt to force sync-to-vblank to reduce tearing, you can use `SDL_RENDERER_PRESENTVSYNC` instead of zero for the third parameter. You shouldn't create a window with the `SDL_WINDOW_OPENGL` flag here. If [SDL_CreateRenderer](SDL_CreateRenderer.md)() decides it wants to use OpenGL, it'll update the window appropriately for you.

Now that you understand how this works, you can also do this all in one step with [SDL_CreateWindowAndRenderer](SDL_CreateWindowAndRenderer.md)(), if you don't want anything fancy:

```c
SDL_Window *sdlWindow;
SDL_Renderer *sdlRenderer;
SDL_CreateWindowAndRenderer(0, 0, SDL_WINDOW_FULLSCREEN_DESKTOP, &sdlWindow, &sdlRenderer);
```

Assuming these functions didn't fail (always check for NULLs!), you are ready to start drawing to the screen. Let's get started by clearing the screen to black.

```c
SDL_SetRenderDrawColor(sdlRenderer, 0, 0, 0, 255);
SDL_RenderClear(sdlRenderer);
SDL_RenderPresent(sdlRenderer);
```

This works like you might think; draw in black (r,g,b all zero, alpha full), clear the whole window, put the cleared window on the screen. That's right, if you've been using `SDL_UpdateRect()` or `SDL_Flip()` to get your bits to the screen, the render API uses [SDL_RenderPresent](SDL_RenderPresent.md)().

One more general thing to set up here. Since we're using `SDL_WINDOW_FULLSCREEN_DESKTOP`, we don't actually _know_ how much screen we've got to draw to. Fortunately, we don't have to know. One of the nice things about 1.2 is that you could say "I want a 640x480 window and I don't care how you get it done," even if getting it done meant centering the window in a larger resolution on behalf of your application.

For 2.0, the render API lets you do this...

```c
SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
SDL_RenderSetLogicalSize(sdlRenderer, 640, 480);
```

...and it will do the right thing for you. This is nice in that you can change the logical rendering size to achieve various effects, but the primary use is this: instead of trying to make the system work with your rendering size, we can now make your rendering size work with the system. On my 1920x1200 monitor, this app thinks it's talking to a 640x480 resolution now, but SDL is using the GPU to scale it up to use all those pixels. Note that 640x480 and 1920x1200 aren't the same aspect ratio: SDL takes care of that, too, scaling as much as possible and letterboxing the difference.

Now we're ready to start drawing for real.


#### If your game just wants to get fully-rendered frames to the screen

A special case for old school software rendered games: the application wants to draw every pixel itself and get that final set of pixels to the screen efficiently in one big blit. An example of a game like this is _Doom_, or _Duke Nukem 3D_, or many others.

For this, you're going to want a single SDL_Texture that will represent the screen. Let's create one now for our 640x480 game:

```c
sdlTexture = SDL_CreateTexture(sdlRenderer,
                               SDL_PIXELFORMAT_ARGB8888,
                               SDL_TEXTUREACCESS_STREAMING,
                               640, 480);
```

This represents a texture on the GPU. The gameplan is to finish each frame by uploading pixels to this texture, drawing the texture to the window, and flipping this drawing onto the screen. `SDL_TEXTUREACCESS_STREAMING` tells SDL that this texture's contents are going to change frequently.

Before you probably had an [SDL_Surface](SDL_Surface.md) for the screen that your app drew into, then called `SDL_Flip()` to put it to the screen. Now you can create an [SDL_Surface](SDL_Surface.md) that is always in RAM instead of using the one you would have gotten from `SDL_SetVideoMode()`, or just `malloc()` a block of pixels to write into. Ideally you write to a buffer of RGBA pixels, but if you need to do a conversion, that's okay too.

```c
extern Uint32 *myPixels;  // maybe this is a surface->pixels, or a malloc()'d buffer, or whatever.
```

At the end of the frame, we want to upload to the texture like this:

```c
SDL_UpdateTexture(sdlTexture, NULL, myPixels, 640 * sizeof (Uint32));
```

This will upload your pixels to GPU memory. That NULL can be a subregion if you want to mess around with dirty rectangles, but chances are modern hardware can just swallow the whole framebuffer without much trouble. The final argument is the pitch--the number of bytes from the start of one row to the next--and since we have a linear RGBA buffer in this example, it's just 640 times 4 (r,g,b,a).

Now get that texture to the screen:

```c
SDL_RenderClear(sdlRenderer);
SDL_RenderCopy(sdlRenderer, sdlTexture, NULL, NULL);
SDL_RenderPresent(sdlRenderer);
```

That's all. [SDL_RenderClear](SDL_RenderClear.md)() wipes out the existing video framebuffer (in case, say, the Steam Overlay wrote over it last frame), [SDL_RenderCopy](SDL_RenderCopy.md)() moves the texture's contents to the video framebuffer (and thanks to [SDL_RenderSetLogicalSize](SDL_RenderSetLogicalSize.md)(), it will be scaled/centered as if the monitor was 640x480), and [SDL_RenderPresent](SDL_RenderPresent.md)() puts it on the screen.


#### If your game wants to blit surfaces to the screen

This scenario has your SDL 1.2 game loading a bunch of graphics from disk into a bunch of [SDL_Surfaces](SDL_Surface.md), possibly trying to get them into video RAM with `SDL_HWSURFACE`. You load these once, and you blit them over and over to the framebuffer as necessary, but otherwise they never change. A simple 2D platformer might do this. If you tend to think of your surfaces as "sprites," and not buffers of pixels, then this is probably you.

You can build individual textures (surfaces that live in GPU memory) like we did for that one big texture:

```c
sdlTexture = SDL_CreateTexture(sdlRenderer,
                               SDL_PIXELFORMAT_ARGB8888,
                               SDL_TEXTUREACCESS_STATIC,
                               myWidth, myHeight);
```

Which does what you'd expect. We use `SDL_TEXTUREACCESS_STATIC`, because we're going to upload our pixels once instead of over and over. But a more convenient solution might be:

```c
sdlTexture = SDL_CreateTextureFromSurface(sdlRenderer, mySurface);
```

Use this, and you load your [SDL_Surface](SDL_Surface.md) as usual, but then at the end you make a texture out of it. Once you have an [SDL_Texture](SDL_Texture.md), you can free the original surface.

At this point, your 1.2 game had a bunch of [SDL_Surfaces](SDL_Surface.md), which it would [SDL_BlitSurface](SDL_BlitSurface.md)() to the screen surface to compose the final framebuffer, and eventually `SDL_Flip()` to the screen. For SDL 2.0, you have a bunch of [SDL_Textures](SDL_Texture.md), that you will [SDL_RenderCopy](SDL_RenderCopy.md)() to your Renderer to compose the final framebuffer, and eventually [SDL_RenderPresent](SDL_RenderPresent.md)() to the screen. It's that simple. If these textures never need modification, you might find your framerate has just gone through the roof, too.


#### If your game wants to do both

Things get slightly more complicated if you want to blit surfaces _and_ modify individual pixels in the framebuffer. Round trips--reading data back from textures--can be painfully expensive; generally you want to be pushing data in one direction always. You are probably best off, in this case, keeping everything in software until the final push to the screen, so we'll combine the two previous techniques.

The good news: the 1.2 [SDL_Surface](SDL_Surface.md) API mostly still exists. So change your screen surface from this:

```c
SDL_Surface *screen = SDL_SetVideoMode(640, 480, 32, 0);
```

...to this...

```c
// if all this hex scares you, check out SDL_PixelFormatEnumToMasks()!
SDL_Surface *screen = SDL_CreateRGBSurface(0, 640, 480, 32,
                                        0x00FF0000,
                                        0x0000FF00,
                                        0x000000FF,
                                        0xFF000000);
SDL_Texture *sdlTexture = SDL_CreateTexture(sdlRenderer,
                                            SDL_PIXELFORMAT_ARGB8888,
                                            SDL_TEXTUREACCESS_STREAMING,
                                            640, 480);
```

...and continue blitting things around and tweaking pixels as before, composing your final framebuffer into this [SDL_Surface](SDL_Surface.md). Once you're ready to get those pixels on the screen, you do this just like in our first scenario:

```c
SDL_UpdateTexture(sdlTexture, NULL, screen->pixels, screen->pitch);
SDL_RenderClear(sdlRenderer);
SDL_RenderCopy(sdlRenderer, sdlTexture, NULL, NULL);
SDL_RenderPresent(sdlRenderer);
```

Note that texture creation may be both expensive and a limited resource: don't call [SDL_CreateTextureFromSurface](SDL_CreateTextureFromSurface.md)() every frame. Set up one texture and one surface and update the former from the latter.

There are more features to the Render API, some of which may be able to replace your application's code: scaling, line drawing, etc. If you are reading this section because you have simple needs beyond blitting surfaces, you might be able to stop poking individual pixels and move everything onto the GPU, which will give your program a significant speed boost and probably simplify your code greatly.

#### Other Renderer API notes

You can do some simple effects with the render API without having to get down into direct pixel manipulation. Some of these were available on 1.2 surfaces.

- Color alpha: [SDL_Color](SDL_Color.md) now contains a fourth, **alpha** component. Your 1.2 code that deals with SDL_Colors might be not copying/setting that value (which was named `unused`). In 2.0, you should.
- Alpha blending: use [SDL_SetSurfaceAlphaMod](SDL_SetSurfaceAlphaMod.md) and [SDL_SetTextureAlphaMod](SDL_SetTextureAlphaMod.md) instead of `SDL_SetAlpha()`. Alpha-blending on surfaces can be disabled via [SDL_SetSurfaceBlendMode](SDL_SetSurfaceBlendMode.md)() and on textures with [SDL_SetTextureBlendMode](SDL_SetTextureBlendMode.md)().
- Colorkey: When calling [SDL_SetColorKey](SDL_SetColorKey.md)(), you should pass `SDL_TRUE` instead of `SDL_SRCCOLORKEY`.
- Color modulation: Some renderers now support a global color alteration (`srcC = srcC * color`), check [SDL_SetTextureColorMod](SDL_SetTextureColorMod.md)() for details.

### OpenGL

If you were already using OpenGL directly, your migration is pretty simple. Change your `SDL_SetVideoMode()` call to [SDL_CreateWindow](SDL_CreateWindow.md)() followed by [SDL_GL_CreateContext](SDL_GL_CreateContext.md)(), and your `SDL_GL_SwapBuffers()` call to [SDL_GL_SwapWindow](SDL_GL_SwapWindow.md)(window). All the actual calls into the GL are exactly the same.

If you had used [SDL_GL_SetAttribute](SDL_GL_SetAttribute.md)(SDL_GL_SWAP_CONTROL, x), this has changed. There is now an [SDL_GL_SetSwapInterval](SDL_GL_SetSwapInterval.md)(x) call, so you can change this on an existing GL context.

Note that SDL 2.0 can toggle windowed/fullscreen and back with OpenGL windows without losing the GL context (hooray!). Use [SDL_SetWindowFullscreen](SDL_SetWindowFullscreen.md)() for this.


### Input

The good news is that SDL 2.0 has made Unicode input usable. The bad news is that it will take some minor changes to your application.

In 1.2, many applications that only cared about US English still called `SDL_EnableUNICODE(1)`, because it was useful to get the character that was associated with a keypress. This didn't work well once you got outside of English, and it really didn't work _at all_ once you got to Asian languages.

It turns out, i18n is hard.

SDL changed this. `SDL_EnableUNICODE()` is gone, and so is [SDL_Keysym](SDL_Keysym.md)'s `unicode` field. You no longer get character input from [SDL_KEYDOWN](SDL_EventType.md) events. Use [SDL_KEYDOWN](SDL_EventType.md) to treat the keyboard like a 101-button joystick now. Text input comes from somewhere else.

The new event is [SDL_TEXTINPUT](SDL_EventType.md). This is triggered whenever there's new text entered by the user. Note that this text might be coming from keypresses, or it might be coming from some sort of IME (which is a fancy way of entering complicated, multi-character text). This event returns entire strings, which might be one char long, or several codepoints of multi-character data. This string is always in UTF-8 encoding.

If all you care about is whether the user pressed a certain key, that's still [SDL_KEYDOWN](SDL_EventType.md), but we've split this system into two pieces since 1.2: keycodes and scancodes.

Scancodes are meant to be layout-independent. Think of this as "the user pressed the Q key as it would be on a US QWERTY keyboard" regardless of whether this is actually a European keyboard or a Dvorak keyboard or whatever. The scancode is always the same key position.

Keycodes are meant to be layout-dependent. Think of this as "the user pressed the key that is labelled 'Q' on their specific keyboard."

In example, if you pressed the key that's two keys to the right of CAPS LOCK on a US QWERTY keyboard, it'll report a scancode of `SDL_SCANCODE_S` and a keycode of `SDLK_S`. The same key on a Dvorak keyboard, will report a scancode of `SDL_SCANCODE_S` and a keycode of `SDLK_O`.

Note that both keycodes and scancodes are now 32 bits, and use a wide range of numbers. There's no `SDLK_LAST` anymore. If your program had a lookup table of `SDLK_LAST` elements, to map between SDL keys and whatever your application wanted internally, that's no longer feasible. Use a hash table instead. A `std::map` will do. If you're mapping scancodes instead of keycodes, there's `SDL_NUM_SCANCODES`, which you can use for array bounds. It's 512 at the moment.

`SDLMod` is now [SDL_Keymod](SDL_Keymod.md) and its "META" keys (the "Windows" keys) are now called the "GUI" keys.

`SDL_GetKeyState()` has been renamed to [SDL_GetKeyboardState](SDL_GetKeyboardState.md)(). The returned array should now be indexed by `SDL_SCANCODE_*` values (see [SDL_Scancode](SDL_Scancode.md)) instead of [SDL_Keysym](SDL_Keysym.md) values.

Now, for mouse input.

The first change, simply enough, is that the mousewheel is no longer a button. This was a mistake of history, and we've corrected it in SDL 2.0. Look for [SDL_MOUSEWHEEL](SDL_EventType.md) events. We support both vertical and horizontal wheels, and some platforms can treat two-finger scrolling on a trackpad as wheel input, too. You will no longer receive [SDL_BUTTONDOWN](SDL_EventType.md) events for mouse wheels, and buttons 4 and 5 are real mouse buttons now.

If your game needed to roll the mouse in one direction forever, for example to let a player in an FPS to spin around without the mouse hitting the edge of the screen and stopping, you probably hid the mouse cursor and grabbed input:

```c
SDL_ShowCursor(0);
SDL_WM_GrabInput(SDL_GRAB_ON);
```

In SDL2, this works slightly differently. You call...

```c
SDL_SetRelativeMouseMode(SDL_TRUE);
```

...and SDL does the rest.


### Events

[SDL_PushEvent](SDL_PushEvent.md)() now returns `1` on success instead of `0`.

Events mask are now specified using ranges:

```c
SDL_PeepEvents(&event, 1, SDL_GETEVENT, SDL_EVENTMASK(SDL_MOUSEBUTTONDOWN));
```

becomes:

```c
SDL_PeepEvents(&event, 1, SDL_GETEVENT, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONDOWN);
```

### Audio

The good news for audio is that, with one exception, it's entirely backwards compatible with 1.2. If you want the new features, they're available to you, but you'll probably just compile and run without them.

That one really important exception: The audio callback does NOT start with a fully initialized buffer anymore. You ***must*** fully write to the buffer in all cases. If you don't have enough audio, your callback should write silence. If you fail to do this, you'll hear repeated audio, or maybe audio corruption. If you want to restore the old behavior of unconditionally initializing the buffer, just put an `SDL_memset(stream, 0, len)` at the start of your callback.


### Joysticks

Joystick events now refer to an SDL_JoystickID. This is because SDL 2.0 can handle joysticks coming and going, as devices are plugged in and pulled out during your game's lifetime, so the index into the device list that 1.2 uses would be meaningless as the available device list changes.

To get an SDL_JoystickID for your opened SDL_Joystick*, call:

```c
SDL_JoystickID myID = SDL_JoystickInstanceID(myOpenedStick);
```

And compare the joystick events' `which` field against `myID`. If you aren't using the event queue for joysticks, [SDL_JoystickGetAxis](SDL_JoystickGetAxis.md)() and friends work just like SDL 1.2.

You should also check out the new [Game Controller API](CategoryGameController) too, because it's cool, and maybe you did a lot of tap dancing with the 1.2 API that this new code would solve more cleanly. You can find it in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h). The Game Controller API integrates really nicely with Steam Big Picture Mode: you get automatic configuration of most controllers, and a nice UI if you have to manually configure it. In either case, Steam passes this configuration on to your SDL application.

Support for the older joystick API (/dev/input/js*) for Linux has been dropped from SDL2. SDL2 only supports the newer events API (/dev/input/event*) for joysticks. These events are not normally readable for normal user accounts, so even if joysticks are plugged in you will likely have none detected. This is something that end users will have to configure for themselves.


### Threads

`SDL_KillThread()` is gone. It was never safe or reliable. The best replacement is to set a flag that tells a thread it should quit. That thread should check the flag with some frequency, and then the "killing" thread calls [SDL_WaitThread](SDL_WaitThread.md)() to clean up.

[SDL_CreateThread](SDL_CreateThread.md)() takes an extra parameter now, a name for the thread, which can be used by debuggers to identify it. If you don't care about that, just stuff an extra NULL into your function call.


### Audio CDs

The 1.2 CD API is completely gone. There's no replacement. Chances are you aren't shipping your music as CD-Audio tracks on a disc at this point, if you're shipping a disc at all, and in modern times, machines don't come with CD players wired to play audio directly, or CD players at all!

You can use [Ogg Vorbis](https://www.vorbis.com/) or some other audio file format for music, many of which are provided by [SDL_mixer](https://github.com/libsdl-org/SDL_mixer).


### Dead platforms

We ripped out a bunch of old platforms, like Windows CE and Mac OS 9. It would be easier to list the ones we still support: Windows (XP and later, and UWP), Linux, macOS, iOS, Android, Emscripten, various console ports. In SDL tradition, there are others on the periphery that work but aren't heavily supported, like Haiku and Sony PSP. We'll add any platform that someone sends patches for, but it seemed like it was time to say goodbye to some old friends when moving to the new version.


### Mobile platforms

There have been, for many years, unofficial ports of SDL 1.2 to iOS and Android. SDL now supports these platforms directly, and the 2.0 API is much better suited to them. Most of the advice you've gotten elsewhere in this document applies, but there are a few other things worth noting.

First, there are certain events that only apply to mobile devices, or better said, apply to the way mobile device OSes tend to operate in a post-iPhone world. We originally tried to map these to the existing SDL events (such as "your application is going to the background" being treated like a desktop window losing focus), but there's a more urgent concern: most of these events need an immediate response, and if the app doesn't give one, the OS will kill your application.

As such, we've added new SDL events for some Android and iOS specific details, but you should set up an SDL event filter to catch them as soon as the OS reports them, because waiting until your next [SDL_PollEvent](SDL_PollEvent.md)() loop will be too late.

For example, there's `SDL_APP_WILLENTERBACKGROUND`, which is iOS's `applicationWillResignActive()`, and if you draw to the screen after this event arrives, iOS terminates your process. So you want to catch this immediately:

```c
int SDLCALL myEventFilter(void *userdata, SDL_Event * event)
{
    if (event->type == SDL_APP_WILLENTERBACKGROUND) {
        // free up resources, DON'T DRAW ANY MORE until you're in the foreground again!
    }
    // etc
    return 1;
}

// somewhere near startup...

// this calls myEventFilter(data, event) as soon as event is generated.
SDL_AddEventWatch(myEventFilter, data);
```

Second, there are real touch events now, instead of trying to map this to mouse input. You can track touches, multiple fingers, and even complex gestures. You probably want to use those. Refer to [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_touch.h) for a list of these functions, and look for [SDL_Finger](SDL_Finger.md)* in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h).

Note that SDL will also map simple touches to look like mouse events (with the mouse event's "which" field set to `SDL_TOUCH_MOUSEID`), which means that if you don't care about more complex touch interfaces, your existing desktop app might still work out of the box on a phone where the user is poking the screen with a finger. As such: mobile-aware apps should probably ignore SDL_TOUCH_MOUSEID events, but still respect "real" mouse events in addition to the touch events--some mobile devices support USB and Bluetooth mice, after all!--but this is something to consider more deeply when you start to polish your app, after you are up and running on SDL2.

There are a handful of other mobile-friendly functions, like [SDL_StartTextInput](SDL_StartTextInput.md)(), which will show the on-screen keyboard. Make use of them.

In addition, there are also Android and iOS specific functions, to let you access platform-specific features that wouldn't make sense in a general API. Refer to [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h) for a list of these functions.


### RWops

[SDL_RWread](SDL_RWread.md)() and [SDL_RWwrite](SDL_RWwrite.md)() now return `0` on error instead of `-1`.

If you wrote your own [SDL_RWops](SDL_RWops.md) implementation, the function signatures have changed. Functions now use `Sint64` and `size_t` instead of `int` so they can work with large files. In many cases, you can just update your function signatures and keep working as before, but if you had bumped up against these limitations, you might be happy to have a solution. Calling applications should know that the return values have changed.

There is also a `size` method to RWops, now. It is called [SDL_RWsize](SDL_RWsize.md)(). This lets a RWops report the size of the stream without having to make the app seek to zero bytes from the end; in other words, you can report a total size for streams that can't seek. For streams that can't even do that, you can still return -1.


### Add-on libraries

The official extensions SDL_image, SDL_ttf, SDL_mixer and SDL_net have a version dedicated to SDL 2.0: SDL2_image, SDL2_ttf, SDL2_mixer and SDL2_net. You may need to download them from the [GitHub repositories](https://github.com/libsdl-org/) for the latest fixes. Subsequently, of course, you will have to link against e.g. SDL2_image, not SDL_image, to compile your program.

These libraries will not be supporting 1.2 going forward, and any compatibility with 1.2 is likely to vanish at some point from newer versions.

[SDL_gfx](https://www.ferzkopp.net/joomla/content/view/19/14/) can also be compiled with 2.0 starting since 2.0.21 (May 2010).


### Summary of some renamed or replaced things

A short cheat sheet where some of the old functions and other stuff went:

- SDL_SetVideoMode(): use [SDL_CreateWindow](SDL_CreateWindow.md)() instead (along with [SDL_CreateRenderer](SDL_CreateRenderer.md)() if you want to do classic 2D rendering and not OpenGL)
- SDL_ListModes(): use [SDL_GetDisplayMode](SDL_GetDisplayMode.md)()/[SDL_GetNumDisplayModes](SDL_GetNumDisplayModes.md)() instead
- SDL_UpdateRect()/SDL_Flip(): use [SDL_RenderPresent](SDL_RenderPresent.md)() instead
- SDL_Surface/2D rendering: surfaces still exist, but it is recommended that instead of using SDL_Surfaces, you use [SDL_Textures](SDL_Texture.md) with a 2D accelerated renderer ([SDL_CreateRenderer](SDL_CreateRenderer.md)()) where possible
- SDL_VideoInfo: use [SDL_GetRendererInfo](SDL_GetRendererInfo.md)()/[SDL_GetRenderDriverInfo](SDL_GetRenderDriverInfo.md)() instead
- SDL_GetCurrentVideoDisplay(): use [SDL_GetWindowDisplayIndex](SDL_GetWindowDisplayIndex.md)() instead
- SDL_VIDEORESIZE event: the new equivalent is [SDL_WINDOWEVENT_RESIZED](SDL_WindowEvent.md)


### Other stuff

There's an enormous amount of new and interesting functionality in SDL 2.0 that 1.2 couldn't even dream of. We've only tried to explain what you might have to do to get your 1.2 program running on 2.0 here, but you should explore the documentation for things that you might have always wished for and, until now, done without. For example, every game I've ever ported ended up with a message box function that looked like this:

```c
#if USING_SDL
fprintf(stderr, "MSGBOX: %s\n%s\n", title, text);   // oh well.
#endif
```

Now there's [SDL_ShowSimpleMessageBox](SDL_ShowSimpleMessageBox.md)(). You're welcome!

If you skipped ahead, go back and check out all the new features [at the overview](#overview-of-new-features)!
