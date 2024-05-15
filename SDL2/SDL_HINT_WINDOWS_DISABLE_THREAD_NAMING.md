###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WINDOWS_DISABLE_THREAD_NAMING

Tell SDL not to name threads on Windows with the 0x406D1388 Exception.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_DISABLE_THREAD_NAMING "SDL_WINDOWS_DISABLE_THREAD_NAMING"
```

## Remarks

The 0x406D1388 Exception is a trick used to inform Visual Studio of a
thread's name, but it tends to cause problems with other debuggers, and the
.NET runtime. Note that SDL 2.0.6 and later will still use the (safer)
SetThreadDescription API, introduced in the Windows 10 Creators Update, if
available.

The variable can be set to the following values:

- "0": SDL will raise the 0x406D1388 Exception to name threads. This is the
  default behavior of SDL <= 2.0.4.
- "1": SDL will not raise this exception, and threads will be unnamed.
  (default) This is necessary with .NET languages or debuggers that aren't
  Visual Studio.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

