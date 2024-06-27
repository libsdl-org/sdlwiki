###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_INVALID_UNICODE_CODEPOINT

The Unicode REPLACEMENT CHARACTER codepoint.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
#define SDL_INVALID_UNICODE_CODEPOINT 0xFFFD
```

## Remarks

[SDL_StepUTF8](SDL_StepUTF8)() reports this codepoint when it encounters a
UTF-8 string with encoding errors.

This tends to render as something like a question mark in most places.

## Version

This macro is available since SDL 3.0.0.

## See Also

- [SDL_StepUTF8](SDL_StepUTF8)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryStdinc](CategoryStdinc)

