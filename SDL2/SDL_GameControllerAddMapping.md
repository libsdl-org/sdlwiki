###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerAddMapping

Add support for controllers that SDL is unaware of or to cause an existing controller to have a different binding.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerAddMapping(const char* mappingString);
```

## Function Parameters

|              |                   |                     |
| ------------ | ----------------- | ------------------- |
| const char * | **mappingString** | the mapping string. |

## Return Value

(int) Returns 1 if a new mapping is added, 0 if an existing mapping is
updated, -1 on error; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The mapping string has the format "GUID,name,mapping", where GUID is the
string value from [SDL_JoystickGetGUIDString](SDL_JoystickGetGUIDString)(),
name is the human readable string for the device and mappings are
controller mappings to joystick ones. Under Windows there is a reserved
GUID of "xinput" that covers all XInput devices. The mapping format for
joystick is: {| |bX |a joystick button, index X |- |hX.Y |hat X with value
Y |- |aX |axis X of the joystick |} Buttons can be used as a controller
axes and vice versa.

This string shows an example of a valid mapping for a controller:

```c
"341a3608000000000000504944564944,Afterglow PS3 Controller,a:b1,b:b2,y:b3,x:b0,start:b9,guide:b12,back:b8,dpup:h0.1,dpleft:h0.8,dpdown:h0.4,dpright:h0.2,leftshoulder:b4,rightshoulder:b5,leftstick:b10,rightstick:b11,leftx:a0,lefty:a1,rightx:a2,righty:a3,lefttrigger:b6,righttrigger:b7"
```

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GameControllerMapping](SDL_GameControllerMapping)
- [SDL_GameControllerMappingForGUID](SDL_GameControllerMappingForGUID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

