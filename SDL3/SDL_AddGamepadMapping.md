###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AddGamepadMapping

Add support for gamepads that SDL is unaware of or change the binding of an existing gamepad.

## Syntax

```c
int SDL_AddGamepadMapping(const char *mapping);

```

## Function Parameters

|                 |                    |
| --------------- | ------------------ |
| **mapping**     | the mapping string |

## Return Value

Returns 1 if a new mapping is added, 0 if an existing mapping is updated,
-1 on error; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The mapping string has the format "GUID,name,mapping", where GUID is the
string value from [SDL_GetJoystickGUIDString](SDL_GetJoystickGUIDString)(),
name is the human readable string for the device and mappings are gamepad
mappings to joystick ones. Under Windows there is a reserved GUID of
"xinput" that covers all XInput devices. The mapping format for joystick
is:

- `bX`: a joystick button, index X
- `hX.Y`: hat X with value Y
- `aX`: axis X of the joystick

Buttons can be used as a gamepad axes and vice versa.

This string shows an example of a valid mapping for a gamepad:

```c
"341a3608000000000000504944564944,Afterglow PS3 Controller,a:b1,b:b2,y:b3,x:b0,start:b9,guide:b12,back:b8,dpup:h0.1,dpleft:h0.8,dpdown:h0.4,dpright:h0.2,leftshoulder:b4,rightshoulder:b5,leftstick:b10,rightstick:b11,leftx:a0,lefty:a1,rightx:a2,righty:a3,lefttrigger:b6,righttrigger:b7"
```

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGamepadMapping](SDL_GetGamepadMapping)
* [SDL_GetGamepadMappingForGUID](SDL_GetGamepadMappingForGUID)

----
[CategoryAPI](CategoryAPI)

