
## Draft

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!


# GameController and Joystick Mapping

'''Include File(s):''' [http://hg.libsdl.org/SDL/file/default/include/SDL_gamecontroller.h SDL_gamecontroller.h]





## Introduction

This category contains functions for handling game controllers and for mapping joysticks to game controller semantics. This is built on top of the existing joystick API.

SDL_Gamepad is an abstraction for gamepads ("controllers") similar to the  xbox360-pad: They have a DPAD, two analog sticks, 4 buttons on the right (often called A, B, X, Y), shoulder buttons (two of which might be axes) and 3 buttons in the middle (Start, Back and usually some kind of logo-button).<br/>
This includes devices that have a similar layout, like the Playstation DualShock Controller, but different button names; SDL_Gamepad uses the naming-conventions of xbox360/XInput for all supported devices, so you'll know that SDL_GAMEPAD_AXIS_LEFTX is always the X-Axis of the left Analog Stick, or SDL_GAMEPAD_BUTTON_B is always the rightmost buttons of the 4 buttons on the right, for example.
This makes providing consistent input bindings (for this kind of device) to your users easy, like "press B to jump, move around with the left analog stick" - with SDL_Joystick (and the underlying APIs like DirectInput) it's impossible to know which SDL (or DirectInput) axis or button corresponds to which physical axis/button on the device.

If you are running your game from Steam, the game controller mapping is automatically provided for your game.

## Enumerations
<<FullSearchCached(category:CategoryGamepad CategoryEnum -title:SGEnumerations)>>


<!-- #== Structures == -->
<!-- #<<FullSearchCached(category:CategoryGamepad CategoryStruct -title:SGStructures)>> -->


## Functions
<<FullSearchCached(category:CategoryGamepad -CategoryEnum -title:CategoryStruct)>>

<!-- BEGIN CATEGORY LIST -->
- [SDL_GameControllerEventState](SDL_GameControllerEventState.md)
- [SDL_GamepadConnected](SDL_GamepadConnected.md)
- [SDL_GameControllerNameForIndex](SDL_GameControllerNameForIndex.md)
<!-- END CATEGORY LIST -->
----
[CategoryCategory](CategoryCategory.md), [CategoryDraft](CategoryDraft.md)
