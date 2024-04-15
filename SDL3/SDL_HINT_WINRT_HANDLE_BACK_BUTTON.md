###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINRT_HANDLE_BACK_BUTTON

A variable controlling whether back-button-press events on Windows Phone to be marked as handled.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_WINRT_HANDLE_BACK_BUTTON "SDL_WINRT_HANDLE_BACK_BUTTON"
```

## Remarks

Windows Phone devices typically feature a Back button. When pressed, the OS
will emit back-button-press events, which apps are expected to handle in an
appropriate manner. If apps do not explicitly mark these events as
'Handled', then the OS will invoke its default behavior for unhandled
back-button-press events, which on Windows Phone 8 and 8.1 is to terminate
the app (and attempt to switch to the previous app, or to the device's home
screen).

Setting the
[SDL_HINT_WINRT_HANDLE_BACK_BUTTON](SDL_HINT_WINRT_HANDLE_BACK_BUTTON) hint
to "1" will cause SDL to mark back-button-press events as Handled, if and
when one is sent to the app.

Internally, Windows Phone sends back button events as parameters to special
back-button-press callback functions. Apps that need to respond to
back-button-press events are expected to register one or more callback
functions for such, shortly after being launched (during the app's
initialization phase). After the back button is pressed, the OS will invoke
these callbacks. If the app's callback(s) do not explicitly mark the event
as handled by the time they return, or if the app never registers one of
these callback, the OS will consider the event un-handled, and it will
apply its default back button behavior (terminate the app).

SDL registers its own back-button-press callback with the Windows Phone OS.
This callback will emit a pair of SDL key-press events
([SDL_EVENT_KEY_DOWN](SDL_EVENT_KEY_DOWN) and
[SDL_EVENT_KEY_UP](SDL_EVENT_KEY_UP)), each with a scancode of
[SDL_SCANCODE_AC_BACK](SDL_SCANCODE_AC_BACK), after which it will check the
contents of the hint,
[SDL_HINT_WINRT_HANDLE_BACK_BUTTON](SDL_HINT_WINRT_HANDLE_BACK_BUTTON). If
the hint's value is set to "1", the back button event's Handled property
will get set to 'true'. If the hint's value is set to something else, or if
it is unset, SDL will leave the event's Handled property alone. (By
default, the OS sets this property to 'false', to note.)

SDL apps can either set
[SDL_HINT_WINRT_HANDLE_BACK_BUTTON](SDL_HINT_WINRT_HANDLE_BACK_BUTTON) well
before a back button is pressed, or can set it in direct-response to a back
button being pressed.

In order to get notified when a back button is pressed, SDL apps should
register a callback function with [SDL_AddEventWatch](SDL_AddEventWatch)(),
and have it listen for [SDL_EVENT_KEY_DOWN](SDL_EVENT_KEY_DOWN) events that
have a scancode of [SDL_SCANCODE_AC_BACK](SDL_SCANCODE_AC_BACK).
(Alternatively, [SDL_EVENT_KEY_UP](SDL_EVENT_KEY_UP) events can be
listened-for. Listening for either event type is suitable.) Any value of
[SDL_HINT_WINRT_HANDLE_BACK_BUTTON](SDL_HINT_WINRT_HANDLE_BACK_BUTTON) set
by such a callback, will be applied to the OS' current back-button-press
event.

More details on back button behavior in Windows Phone apps can be found at
the following page, on Microsoft's developer site:
http://msdn.microsoft.com/en-us/library/windowsphone/develop/jj247550(v=vs.105).aspx

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryHints]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


