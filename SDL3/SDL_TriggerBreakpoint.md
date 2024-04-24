###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TriggerBreakpoint

Attempt to tell an attached debugger to pause.

## Header File

Defined in [<SDL3/SDL_assert.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_assert.h)

## Syntax

```c
#define SDL_TriggerBreakpoint() TriggerABreakpointInAPlatformSpecificManner
```

## Remarks

This allows an app to programmatically halt ("break") the debugger as if it
had hit a breakpoint, allowing the developer to examine program state, etc.

This is a macro--not a function--so that the debugger breaks on the source
code line that used [SDL_TriggerBreakpoint](SDL_TriggerBreakpoint) and not
in some random guts of SDL. [SDL_assert](SDL_assert) uses this macro for
the same reason.

If the program is not running under a debugger,
[SDL_TriggerBreakpoint](SDL_TriggerBreakpoint) will likely terminate the
app, possibly without warning. If the current platform isn't supported (SDL
doesn't know how to trigger a breakpoint), this macro does nothing.

## Thread Safety

It is safe to call this function from any thread.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

