# SDL_HINT_ANDROID_ALLOW_PERSISTENT_FOLDER_ACCESS

A variable to control whether we allow persistent folder access on Android when using the SDL select folder dialog.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ANDROID_ALLOW_PERSISTENT_FOLDER_ACCESS "SDL_ANDROID_ALLOW_PERSISTENT_FOLDER_ACCESS"
```

## Remarks

If set to `1`, the selected folder will be accessible persistently across
app launches. That allows the user to only have to select the directory
once, and then the app can access it again in the future without needing to
ask the user to select it again.

The variable can be set to the following values:

- "0": Persistent folder access is not allowed. (default)
- "1": Persistent folder access is allowed.

This hint should be set before the SDL folder selection dialog is shown,
and can be changed between dialog invocations.

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

