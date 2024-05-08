###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINRT_PRIVACY_POLICY_LABEL

A variable specifying the label text for a WinRT app's privacy policy link.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINRT_PRIVACY_POLICY_LABEL "SDL_WINRT_PRIVACY_POLICY_LABEL"
```

## Remarks

Network-enabled WinRT apps must include a privacy policy. On Windows 8,
8.1, and RT, Microsoft mandates that this policy be available via the
Windows Settings charm. SDL provides code to add a link there, with its
label text being set via the optional hint,
[SDL_HINT_WINRT_PRIVACY_POLICY_LABEL](SDL_HINT_WINRT_PRIVACY_POLICY_LABEL).

Please note that a privacy policy's contents are not set via this hint. A
separate hint,
[SDL_HINT_WINRT_PRIVACY_POLICY_URL](SDL_HINT_WINRT_PRIVACY_POLICY_URL), is
used to link to the actual text of the policy.

The contents of this hint should be encoded as a UTF8 string.

The default value is "Privacy Policy".

For additional information on linking to a privacy policy, see the
documentation for
[SDL_HINT_WINRT_PRIVACY_POLICY_URL](SDL_HINT_WINRT_PRIVACY_POLICY_URL).

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

