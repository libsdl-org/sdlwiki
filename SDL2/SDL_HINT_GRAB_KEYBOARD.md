###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGEnumerations for details on editing this page*^*^*^*^* -->
# SDL_HINT_GRAB_KEYBOARD

A variable controlling whether grabbing input grabs the keyboard

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GRAB_KEYBOARD              "SDL_GRAB_KEYBOARD"
```

## Remarks

This variable can be set to the following values: "0" - Grab will affect
only the mouse "1" - Grab will affect mouse and keyboard

By default SDL will not grab the keyboard so system shortcuts still work.

## Default

By default SDL will not grab the keyboard so system shortcuts still work.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


