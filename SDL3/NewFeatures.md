# New Features in SDL3

If you've got an SDL2 app, you might be wondering if you should move to SDL3, or maybe just drop [sdl2-compat](https://github.com/libsdl-org/sdl2-compat) into the mix.

A lot of things you're already using in SDL2 are easier, more consistent, and just generally _better_ in SDL3, so the upgrade can be worth it in any case, but here are some things that are _new features_ in SDL3 that you might want access to:

- [Dialog API](CategoryDialog): access to system file dialogs (file and folder selection UI for opening/saving).
- [Filesystem API](CategoryFilesystem): simple directory management and globbing.
- [Storage API](CategoryStorage): Abstract interface to platform-specific storage.
- [Camera API](CategoryCamera): access to webcams.
- [Main Callbacks](README/main-functions#main-callbacks-in-sdl3): _optionally_ run your program from callbacks instead of `main()`.
- [Pen API](CategoryPen): access to pens (like Wacom tablets and Apple Pencil, etc).
- [The new audio subsystem](CategoryAudio): mix multiple audio streams on logical devices. A good visual summary is [on YouTube](https://www.youtube.com/watch?v=MLau3hWJBeE).
- [Time API](CategoryTime): date and time functionality beyond ticks and performance counters.
- [Properties API](CategoryProperties): fast, flexible dictionaries of name/value pairs.
- [Colorspace support](SDL_Colorspace): Surfaces and the renderer, etc, can manage multiple colorspaces.
- The Clipboard API [can support any data type](SDL_SetClipboardData) (SDL2 only handled text), and apps can provide data in multiple formats upon request in [a provided callback](SDL_ClipboardDataCallback).
- Multiple [keyboards](SDL_GetKeyboards) and [mice](SDL_GetMice) can be managed separately.
- [System theme](SDL_GetSystemTheme) (light, dark) can be queried.
- HiDPI support is dramatically improved over SDL2.
- (More new features are still coming to SDL3, so check back here later!)

If you are looking to move to SDL3 so you can start using these new features, you should take a look at [README/migration](README/migration) for all the little details.

