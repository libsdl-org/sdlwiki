# FAQ: Using SDL3

## How do I choose a specific video/audio/render driver?

You can set an environment variable to the name of the driver you want to use.
The drivers available depend on the platform and SDL compile-time options.

- For video: set `SDL_VIDEO_DRIVER`. Some possible options are "x11", "wayland",
  "cocoa", etc.
- For audio: set `SDL_AUDIO_DRIVER`. Some possible options are "pipewire",
  "pulseaudio", "directsound", "wasapi".
  "cocoa", etc.
- For render: `SDL_RENDER_DRIVER`. Some possible options are "opengl",
  "direct3d", "software".

Note that in SDL 1.2 and SDL2, there was one less underscore: `SDL_VIDEODRIVER`.
This legacy variable name is _ignored_ in SDL3!

While an application could force this with SDL_SetHint(), we _strongly_
encourage you not to do this; let SDL choose the best option, and let the user
use the environment variable if they have specific needs; applications usually
shouldn't get involved in this choice.

(The exception is if the program needs to do something specific with a
windowing system: for example, it needs to force the X11 driver because it
is using a library that needs to talk to an X server. But in these cases, we'd
also strongly encourage you to consider that as a bug to be fixed urgently.)


# What environment variables are used by SDL?

A complete list is available in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h).
These can be set programmatically with SDL_SetHint, or specified as enviroment
variables by the end-user.


# Why does SDL disable my screensaver by default?

Many applications using SDL are games or screensavers or media players where
the user is either watching something for an extended period of time or using
joystick input which generally does not prevent the screensaver from kicking
on.

You can disable this behavior by setting the environment variable:
`SDL_VIDEO_ALLOW_SCREENSAVER=1`

This can be set globally for the user or on a per-application basis in code.

Programmatically, the function [SDL_EnableScreenSaver](SDL_EnableScreenSaver)
can be used; this might make sense for some programs to universally enable
the screensaver, or toggle it to disabled only during media playback, etc.

