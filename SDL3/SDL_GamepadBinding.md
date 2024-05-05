###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GamepadBinding

A mapping between one joystick input to a gamepad control.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
typedef struct SDL_GamepadBinding
{
    SDL_GamepadBindingType input_type;
    union
    {
        int button;

        struct
        {
            int axis;
            int axis_min;
            int axis_max;
        } axis;

        struct
        {
            int hat;
            int hat_mask;
        } hat;

    } input;

    SDL_GamepadBindingType output_type;
    union
    {
        SDL_GamepadButton button;

        struct
        {
            SDL_GamepadAxis axis;
            int axis_min;
            int axis_max;
        } axis;

    } output;
} SDL_GamepadBinding;
```

## Remarks

A gamepad has a collection of several bindings, to say, for example, when
joystick button number 5 is pressed, that should be treated like the
gamepad's "start" button.

SDL has these bindings built-in for many popular controllers, and can add
more with a simple text string. Those strings are parsed into a collection
of these structs to make it easier to operate on the data.

## Version

This struct is available since SDL 3.0.0.

## See Also

- [SDL_GetGamepadBindings](SDL_GetGamepadBindings)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

