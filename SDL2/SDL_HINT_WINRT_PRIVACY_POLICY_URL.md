###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WINRT_PRIVACY_POLICY_URL

A URL to a WinRT app's privacy policy

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINRT_PRIVACY_POLICY_URL "SDL_WINRT_PRIVACY_POLICY_URL"
```

## Remarks

All network-enabled WinRT apps must make a privacy policy available to its
users. On Windows 8, 8.1, and RT, Microsoft mandates that this policy be be
available in the Windows Settings charm, as accessed from within the app.
SDL provides code to add a URL-based link there, which can point to the
app's privacy policy.

To setup a URL to an app's privacy policy, set
[SDL_HINT_WINRT_PRIVACY_POLICY_URL](SDL_HINT_WINRT_PRIVACY_POLICY_URL)
before calling any [SDL_Init](SDL_Init)() functions. The contents of the
hint should be a valid URL. For example, "http://www.example.com".

The default value is "", which will prevent SDL from adding a privacy
policy link to the Settings charm. This hint should only be set during app
init.

The label text of an app's "Privacy Policy" link may be customized via
another hint,
[SDL_HINT_WINRT_PRIVACY_POLICY_LABEL](SDL_HINT_WINRT_PRIVACY_POLICY_LABEL).

Please note that on Windows Phone, Microsoft does not provide standard UI
for displaying a privacy policy link, and as such,
[SDL_HINT_WINRT_PRIVACY_POLICY_URL](SDL_HINT_WINRT_PRIVACY_POLICY_URL) will
not get used on that platform. Network-enabled phone apps should display
their privacy policy through some other, in-app means.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 

