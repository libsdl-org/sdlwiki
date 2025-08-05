# SDL_GameControllerButton

The list of buttons available from a controller

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
typedef enum SDL_GameControllerButton
{
    SDL_CONTROLLER_BUTTON_INVALID = -1,
    SDL_CONTROLLER_BUTTON_A,
    SDL_CONTROLLER_BUTTON_B,
    SDL_CONTROLLER_BUTTON_X,
    SDL_CONTROLLER_BUTTON_Y,
    SDL_CONTROLLER_BUTTON_BACK,
    SDL_CONTROLLER_BUTTON_GUIDE,
    SDL_CONTROLLER_BUTTON_START,
    SDL_CONTROLLER_BUTTON_LEFTSTICK,
    SDL_CONTROLLER_BUTTON_RIGHTSTICK,
    SDL_CONTROLLER_BUTTON_LEFTSHOULDER,
    SDL_CONTROLLER_BUTTON_RIGHTSHOULDER,
    SDL_CONTROLLER_BUTTON_DPAD_UP,
    SDL_CONTROLLER_BUTTON_DPAD_DOWN,
    SDL_CONTROLLER_BUTTON_DPAD_LEFT,
    SDL_CONTROLLER_BUTTON_DPAD_RIGHT,
    SDL_CONTROLLER_BUTTON_MISC1,    /* Xbox Series X share button, PS5 microphone button, Nintendo Switch Pro capture button, Amazon Luna microphone button */
    SDL_CONTROLLER_BUTTON_PADDLE1,  /* Xbox Elite paddle P1, PS5 DualSense Edge RB button, Nintendo Switch Joy-Con (L) SR, Steam Deck L4 button (upper left, facing the back) */
    SDL_CONTROLLER_BUTTON_PADDLE2,  /* Xbox Elite paddle P3, PS5 DualSense Edge LB button, Nintendo Switch Joy-Con (L) SL, Steam Deck L5 button (upper right, facing the back) */
    SDL_CONTROLLER_BUTTON_PADDLE3,  /* Xbox Elite paddle P2, Nintendo Switch Joy-Con (R) SR button, Steam Deck R4 button (lower left, facing the back) */
    SDL_CONTROLLER_BUTTON_PADDLE4,  /* Xbox Elite paddle P4, Nintendo Switch Joy-Con (R) SR button, Steam Deck R5 button (lower right, facing the back) */
    SDL_CONTROLLER_BUTTON_TOUCHPAD, /* PS4/PS5 touchpad button */
    SDL_CONTROLLER_BUTTON_MAX
} SDL_GameControllerButton;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGameController](CategoryGameController)

