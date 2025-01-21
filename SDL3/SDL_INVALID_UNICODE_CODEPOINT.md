###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_INVALID_UNICODE_CODEPOINT

The Unicode REPLACEMENT CHARACTER codepoint.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_INVALID_UNICODE_CODEPOINT 0xFFFD
```

## Remarks

[SDL_StepUTF8](SDL_StepUTF8)() and [SDL_StepBackUTF8](SDL_StepBackUTF8)()
report this codepoint when they encounter a UTF-8 string with encoding
errors.

This tends to render as something like a question mark in most places.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_StepBackUTF8](SDL_StepBackUTF8)
- [SDL_StepUTF8](SDL_StepUTF8)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

