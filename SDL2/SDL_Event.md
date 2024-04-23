###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Event

General event structure

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
typedef union SDL_Event
{
    Uint32 type;                            /**< Event type, shared with all events */
    SDL_CommonEvent common;                 /**< Common event data */
    SDL_DisplayEvent display;               /**< Display event data */
    SDL_WindowEvent window;                 /**< Window event data */
    SDL_KeyboardEvent key;                  /**< Keyboard event data */
    SDL_TextEditingEvent edit;              /**< Text editing event data */
    SDL_TextEditingExtEvent editExt;        /**< Extended text editing event data */
    SDL_TextInputEvent text;                /**< Text input event data */
    SDL_MouseMotionEvent motion;            /**< Mouse motion event data */
    SDL_MouseButtonEvent button;            /**< Mouse button event data */
    SDL_MouseWheelEvent wheel;              /**< Mouse wheel event data */
    SDL_JoyAxisEvent jaxis;                 /**< Joystick axis event data */
    SDL_JoyBallEvent jball;                 /**< Joystick ball event data */
    SDL_JoyHatEvent jhat;                   /**< Joystick hat event data */
    SDL_JoyButtonEvent jbutton;             /**< Joystick button event data */
    SDL_JoyDeviceEvent jdevice;             /**< Joystick device change event data */
    SDL_JoyBatteryEvent jbattery;           /**< Joystick battery event data */
    SDL_ControllerAxisEvent caxis;          /**< Game Controller axis event data */
    SDL_ControllerButtonEvent cbutton;      /**< Game Controller button event data */
    SDL_ControllerDeviceEvent cdevice;      /**< Game Controller device event data */
    SDL_ControllerTouchpadEvent ctouchpad;  /**< Game Controller touchpad event data */
    SDL_ControllerSensorEvent csensor;      /**< Game Controller sensor event data */
    SDL_AudioDeviceEvent adevice;           /**< Audio device event data */
    SDL_SensorEvent sensor;                 /**< Sensor event data */
    SDL_QuitEvent quit;                     /**< Quit request event data */
    SDL_UserEvent user;                     /**< Custom event data */
    SDL_SysWMEvent syswm;                   /**< System dependent window event data */
    SDL_TouchFingerEvent tfinger;           /**< Touch finger event data */
    SDL_MultiGestureEvent mgesture;         /**< Gesture event data */
    SDL_DollarGestureEvent dgesture;        /**< Gesture event data */
    SDL_DropEvent drop;                     /**< Drag and drop event data */

    /* This is necessary for ABI compatibility between Visual C++ and GCC.
       Visual C++ will respect the push pack pragma and use 52 bytes (size of
       SDL_TextEditingEvent, the largest structure for 32-bit and 64-bit
       architectures) for this union, and GCC will use the alignment of the
       largest datatype within the union, which is 8 bytes on 64-bit
       architectures.

       So... we'll add padding to force the size to be 56 bytes for both.

       On architectures where pointers are 16 bytes, this needs rounding up to
       the next multiple of 16, 64, and on architectures where pointers are
       even larger the size of SDL_UserEvent will dominate as being 3 pointers.
    */
    Uint8 padding[sizeof(void *) <= 8 ? 56 : sizeof(void *) == 16 ? 64 : 3 * sizeof(void *)];
} SDL_Event;
```

## Data Fields

|                                                        |                |                                        |
| ------------------------------------------------------ | -------------- | -------------------------------------- |
| Uint32                                                 | '''type'''     | event type, shared with all events     |
| [SDL_CommonEvent](SDL_CommonEvent)                     | '''common'''   | common event data                      |
| [SDL_DisplayEvent](SDL_DisplayEvent)                   | '''display'''  | display event data                     |
| [SDL_WindowEvent](SDL_WindowEvent)                     | '''window'''   | window event data                      |
| [SDL_KeyboardEvent](SDL_KeyboardEvent)                 | '''key'''      | keyboard event data                    |
| [SDL_TextEditingEvent](SDL_TextEditingEvent)           | '''edit'''     | text editing event data                |
| [SDL_TextInputEvent](SDL_TextInputEvent)               | '''text'''     | text input event data                  |
| [SDL_MouseMotionEvent](SDL_MouseMotionEvent)           | '''motion'''   | mouse motion event data                |
| [SDL_MouseButtonEvent](SDL_MouseButtonEvent)           | '''button'''   | mouse button event data                |
| [SDL_MouseWheelEvent](SDL_MouseWheelEvent)             | '''wheel'''    | mouse wheel event data                 |
| [SDL_JoyAxisEvent](SDL_JoyAxisEvent)                   | '''jaxis'''    | joystick axis event data               |
| [SDL_JoyBallEvent](SDL_JoyBallEvent)                   | '''jball'''    | joystick ball event data               |
| [SDL_JoyHatEvent](SDL_JoyHatEvent)                     | '''jhat'''     | joystick hat event data                |
| [SDL_JoyButtonEvent](SDL_JoyButtonEvent)               | '''jbutton'''  | joystick button event data             |
| [SDL_JoyDeviceEvent](SDL_JoyDeviceEvent)               | '''jdevice'''  | joystick device event data             |
| [SDL_ControllerAxisEvent](SDL_ControllerAxisEvent)     | '''caxis'''    | game controller axis event data        |
| [SDL_ControllerButtonEvent](SDL_ControllerButtonEvent) | '''cbutton'''  | game controller button event data      |
| [SDL_ControllerDeviceEvent](SDL_ControllerDeviceEvent) | '''cdevice'''  | game controller device event data      |
| [SDL_AudioDeviceEvent](SDL_AudioDeviceEvent)           | '''adevice'''  | audio device event data (>= SDL 2.0.4) |
| [SDL_QuitEvent](SDL_QuitEvent)                         | '''quit'''     | quit request event data                |
| [SDL_UserEvent](SDL_UserEvent)                         | '''user'''     | custom event data                      |
| [SDL_SysWMEvent](SDL_SysWMEvent)                       | '''syswm'''    | system dependent window event data     |
| [SDL_TouchFingerEvent](SDL_TouchFingerEvent)           | '''tfinger'''  | touch finger event data                |
| [SDL_MultiGestureEvent](SDL_MultiGestureEvent)         | '''mgesture''' | multi finger gesture data              |
| [SDL_DollarGestureEvent](SDL_DollarGestureEvent)       | '''dgesture''' | multi finger gesture data              |
| [SDL_DropEvent](SDL_DropEvent)                         | '''drop'''     | drag and drop event data               |

## Related Enumerations

[SDL_EventType](SDL_EventType)

## Related Structures

[SDL_AudioDeviceEvent](SDL_AudioDeviceEvent)
[SDL_ControllerAxisEvent](SDL_ControllerAxisEvent)
[SDL_ControllerButtonEvent](SDL_ControllerButtonEvent)
[SDL_ControllerDeviceEvent](SDL_ControllerDeviceEvent)
[SDL_DollarGestureEvent](SDL_DollarGestureEvent)
[SDL_DropEvent](SDL_DropEvent)
[SDL_JoyAxisEvent](SDL_JoyAxisEvent)
[SDL_JoyBallEvent](SDL_JoyBallEvent)
[SDL_JoyButtonEvent](SDL_JoyButtonEvent)
[SDL_JoyDeviceEvent](SDL_JoyDeviceEvent)
[SDL_JoyHatEvent](SDL_JoyHatEvent)
[SDL_KeyboardEvent](SDL_KeyboardEvent)
[SDL_MouseButtonEvent](SDL_MouseButtonEvent)
[SDL_MouseMotionEvent](SDL_MouseMotionEvent)
[SDL_MouseWheelEvent](SDL_MouseWheelEvent)
[SDL_MultiGestureEvent](SDL_MultiGestureEvent)
[SDL_QuitEvent](SDL_QuitEvent)
[SDL_SysWMEvent](SDL_SysWMEvent)
[SDL_TextEditingEvent](SDL_TextEditingEvent)
[SDL_TextInputEvent](SDL_TextInputEvent)
[SDL_TouchFingerEvent](SDL_TouchFingerEvent)
[SDL_UserEvent](SDL_UserEvent)
[SDL_WindowEvent](SDL_WindowEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)


