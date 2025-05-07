# New Features in SDL3

If you've got an SDL2 app, you might be wondering if you should move to SDL3, or maybe just drop [sdl2-compat](https://github.com/libsdl-org/sdl2-compat) into the mix.

A lot of things you're already using in SDL2 are easier, more consistent, and just generally _better_ in SDL3, so the upgrade can be worth it in any case, but here are some things that are _new features_ in SDL3 that you might want access to:

- [Extremely good documentation](APIByCategory): We've spent a _ton_ of effort writing and revising the API reference.
- [Example programs](https://github.com/libsdl-org/SDL/tree/main/examples) to get you started, [running in your web browser](https://examples.libsdl.org/)!
- More consistent API naming conventions. Everything is named consistently across the API now, instead of different subsystems taking different approaches. Also, we've tended toward more descriptive names for things in SDL3.
- [Main Callbacks](README-main-functions#main-callbacks-in-sdl3): _optionally_ run your program from callbacks instead of `main()`.
- [GPU API](CategoryGPU): access to modern 3D rendering and GPU compute in a cross-platform way.
- [Dialog API](CategoryDialog): access to system file dialogs (file and folder selection UI for opening/saving).
- [Filesystem API](CategoryFilesystem): simple directory management and globbing, access to topic-specific user folders.
- [Storage API](CategoryStorage): Abstract interface to platform-specific storage.
- [Camera API](CategoryCamera): access to webcams.
- [Pen API](CategoryPen): access to pens (like Wacom tablets and Apple Pencil, etc).
- [Logical audio devices](SDL_OpenAudioDevice): different parts of an app can get their own unique audio device to use.
- [Audio streams](SDL_CreateAudioStream): handle buffering, converting, resampling, mixing, channel mapping, pitch, and gain. Bind to an audio device and go!
- [Default audio devices](SDL_AUDIO_DEVICE_DEFAULT_PLAYBACK): SDL3 will automatically manage migrating to new physical hardware as devices are plugged in, ripped out, or changed.
- [Asynchronous I/O](CategoryAsyncIO): Start file reads/writes, come back later to get the results. Can use Windows IoRing and Linux io_uring behind the scenes!
- [Time API](CategoryTime): date and time functionality beyond ticks and performance counters.
- [Properties API](CategoryProperties): fast, flexible dictionaries of name/value pairs.
- [Process API](CategoryProcess): Spawn child processes and communicate with them in various ways.
- [Colorspace support](SDL_Colorspace): Surfaces and the renderer, etc, can manage multiple colorspaces.
- [Alternate surface representations](SDL_AddSurfaceAlternateImage) for embedding HiDPI versions of images into a single SDL_Surface.
- The Clipboard API [can support any data type](SDL_SetClipboardData) (SDL2 only handled text), and apps can provide data in multiple formats upon request in [a provided callback](SDL_ClipboardDataCallback).
- Multiple [keyboards](SDL_GetKeyboards) and [mice](SDL_GetMice) can be managed separately.
- [System theme](SDL_GetSystemTheme) (light, dark) can be queried.
- [Better keyboard input](BestKeyboardPractices), for all your keypress needs.
- [Customizable virtual keyboards](SDL_StartTextInputWithProperties) on iOS and Android.
- [Unicode-friendly case-insensitive string comparison](SDL_strcasecmp).
- HiDPI support is dramatically improved over SDL2.
- [System Tray API](CategoryTray): Create custom system tray/notification area icons and menus.
- [App metadata API](SDL_SetAppMetadata) for letting SDL report things about your app correctly (like in the About dialog on macOS, etc).
- [Read/write thread locks](SDL_CreateRWLock), to let multiple threads access rarely-changing data in parallel.
- [Init State](SDL_InitState) to help with multiple threads that might need to initialize something on-demand without racing.
- 64-bit [SDL_GetTicks](SDL_GetTicks): No more worrying about timer wraparound every ~49 days!
- [SDL_GetTicksNS](SDL_GetTicksNS): when milliseconds won't cut it, you can use nanoseconds!
- [SDL_DelayPrecise](SDL_DelayPrecise): Nanosecond-precision waits, using a mixture of OS-level sleeps and busy-waits.
- [SDL_RunOnMainThread](SDL_RunOnMainThread): dispatch arbitrary code to the main thread, for those pesky OS requirements.
- [Async windowing](SDL_SyncWindow)
- (More new features are still coming to SDL3, so check back here later!)

If you are looking to move to SDL3 so you can start using these new features, you should take a look at [README-migration](README-migration) for all the details.

