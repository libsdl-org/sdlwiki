###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_ANDROID_APK_EXPANSION_PATCH_FILE_VERSION

Android APK expansion patch file version.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ANDROID_APK_EXPANSION_PATCH_FILE_VERSION "SDL_ANDROID_APK_EXPANSION_PATCH_FILE_VERSION"
```

## Remarks

Should be a string number like "1", "2" etc.

Must be set together with
[SDL_HINT_ANDROID_APK_EXPANSION_MAIN_FILE_VERSION](SDL_HINT_ANDROID_APK_EXPANSION_MAIN_FILE_VERSION).

If both hints were set then [SDL_RWFromFile](SDL_RWFromFile)() will look
into expansion files after a given relative path was not found in the
internal storage and assets.

By default this hint is not set and the APK expansion files are not
searched.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)


