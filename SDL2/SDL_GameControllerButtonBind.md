###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGStructures for details on editing this page*^*^*^*^* -->
# SDL_GameControllerButtonBind

Get the SDL joystick layer binding for this controller button/axis mapping

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
typedef struct SDL_GameControllerButtonBind
{
    SDL_GameControllerBindType bindType;
    union
    {
        int button;
        int axis;
        struct {
            int hat;
            int hat_mask;
        } hat;
    } value;

} SDL_GameControllerButtonBind;
```

## Data Fields

{|
|[[SDL_GameControllerBindType]]
|'''bindType'''
|What kind of control this maps to (button/axis/hat/not mapped)
|-
|int
|'''button'''
|The [[SDL_JoystickGetButton|SDL_Joystick button]] this maps to
|-
|int
|'''axis'''
|The [[SDL_JoystickGetAxis|SDL_Joystick axis]] this maps to
|-
|int
|'''hat.hat'''
|The [[SDL_JoystickGetHat|SDL_Joystick hat]] this maps to
|-
|int
|'''hat.hat_mask'''
|the mask you need to binary-& with the hat's value with (this probaly corresponds to '''one''' direction of the hat)
|}

## Related Enumerations

:[[SDL_GameControllerBindType]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryHeader](CategoryHeader), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


