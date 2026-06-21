# SDL_PROP_GLOBAL_SYSTEM_UBUNTU_TOUCH_HOOK_STRING

The identifier for the specific hook which launched the current executable, as reported in the manifest.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
#define SDL_PROP_GLOBAL_SYSTEM_UBUNTU_TOUCH_HOOK_STRING "SDL.system.ubuntu_touch.hook"
```

## Remarks

This is relevant for application packages that ship multiple applications
with their desktop files; they will have the same app ID but will differ by
their hook.

## Version

This macro is available since SDL 3.6.0.

## See Also

- [SDL_IsUbuntuTouch](SDL_IsUbuntuTouch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategorySystem](CategorySystem)

