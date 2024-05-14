###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadButton

The list of buttons available on a gamepad

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
typedef enum SDL_GamepadButton
{
    SDL_GAMEPAD_BUTTON_INVALID = -1,
    SDL_GAMEPAD_BUTTON_SOUTH,           /* Bottom face button (e.g. Xbox A button) */
    SDL_GAMEPAD_BUTTON_EAST,            /* Right face button (e.g. Xbox B button) */
    SDL_GAMEPAD_BUTTON_WEST,            /* Left face button (e.g. Xbox X button) */
    SDL_GAMEPAD_BUTTON_NORTH,           /* Top face button (e.g. Xbox Y button) */
    SDL_GAMEPAD_BUTTON_BACK,
    SDL_GAMEPAD_BUTTON_GUIDE,
    SDL_GAMEPAD_BUTTON_START,
    SDL_GAMEPAD_BUTTON_LEFT_STICK,
    SDL_GAMEPAD_BUTTON_RIGHT_STICK,
    SDL_GAMEPAD_BUTTON_LEFT_SHOULDER,
    SDL_GAMEPAD_BUTTON_RIGHT_SHOULDER,
    SDL_GAMEPAD_BUTTON_DPAD_UP,
    SDL_GAMEPAD_BUTTON_DPAD_DOWN,
    SDL_GAMEPAD_BUTTON_DPAD_LEFT,
    SDL_GAMEPAD_BUTTON_DPAD_RIGHT,
    SDL_GAMEPAD_BUTTON_MISC1,           /* Additional button (e.g. Xbox Series X share button, PS5 microphone button, Nintendo Switch Pro capture button, Amazon Luna microphone button, Google Stadia capture button) */
    SDL_GAMEPAD_BUTTON_RIGHT_PADDLE1,   /* Upper or primary paddle, under your right hand (e.g. Xbox Elite paddle P1) */
    SDL_GAMEPAD_BUTTON_LEFT_PADDLE1,    /* Upper or primary paddle, under your left hand (e.g. Xbox Elite paddle P3) */
    SDL_GAMEPAD_BUTTON_RIGHT_PADDLE2,   /* Lower or secondary paddle, under your right hand (e.g. Xbox Elite paddle P2) */
    SDL_GAMEPAD_BUTTON_LEFT_PADDLE2,    /* Lower or secondary paddle, under your left hand (e.g. Xbox Elite paddle P4) */
    SDL_GAMEPAD_BUTTON_TOUCHPAD,        /* PS4/PS5 touchpad button */
    SDL_GAMEPAD_BUTTON_MISC2,           /* Additional button */
    SDL_GAMEPAD_BUTTON_MISC3,           /* Additional button */
    SDL_GAMEPAD_BUTTON_MISC4,           /* Additional button */
    SDL_GAMEPAD_BUTTON_MISC5,           /* Additional button */
    SDL_GAMEPAD_BUTTON_MISC6,           /* Additional button */
    SDL_GAMEPAD_BUTTON_MAX
} SDL_GamepadButton;
```

## Remarks

For controllers that use a diamond pattern for the face buttons, the
south/east/west/north buttons below correspond to the locations in the
diamond pattern. For Xbox controllers, this would be A/B/X/Y, for Nintendo
Switch controllers, this would be B/A/Y/X, for PlayStation controllers this
would be Cross/Circle/Square/Triangle.

For controllers that don't use a diamond pattern for the face buttons, the
south/east/west/north buttons indicate the buttons labeled A, B, C, D, or
1, 2, 3, 4, or for controllers that aren't labeled, they are the primary,
secondary, etc. buttons.

The activate action is often the south button and the cancel action is
often the east button, but in some regions this is reversed, so your game
should allow remapping actions based on user preferences.

You can query the labels for the face buttons using
[SDL_GetGamepadButtonLabel](SDL_GetGamepadButtonLabel)()

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGamepad](CategoryGamepad)

