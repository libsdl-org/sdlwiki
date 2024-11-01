###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_Event

The structure for all events in SDL.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
typedef union SDL_Event
{
    Uint32 type;                            /**< Event type, shared with all events, Uint32 to cover user events which are not in the SDL_EventType enumeration */
    SDL_CommonEvent common;                 /**< Common event data */
    SDL_DisplayEvent display;               /**< Display event data */
    SDL_WindowEvent window;                 /**< Window event data */
    SDL_KeyboardDeviceEvent kdevice;        /**< Keyboard device change event data */
    SDL_KeyboardEvent key;                  /**< Keyboard event data */
    SDL_TextEditingEvent edit;              /**< Text editing event data */
    SDL_TextEditingCandidatesEvent edit_candidates; /**< Text editing candidates event data */
    SDL_TextInputEvent text;                /**< Text input event data */
    SDL_MouseDeviceEvent mdevice;           /**< Mouse device change event data */
    SDL_MouseMotionEvent motion;            /**< Mouse motion event data */
    SDL_MouseButtonEvent button;            /**< Mouse button event data */
    SDL_MouseWheelEvent wheel;              /**< Mouse wheel event data */
    SDL_JoyDeviceEvent jdevice;             /**< Joystick device change event data */
    SDL_JoyAxisEvent jaxis;                 /**< Joystick axis event data */
    SDL_JoyBallEvent jball;                 /**< Joystick ball event data */
    SDL_JoyHatEvent jhat;                   /**< Joystick hat event data */
    SDL_JoyButtonEvent jbutton;             /**< Joystick button event data */
    SDL_JoyBatteryEvent jbattery;           /**< Joystick battery event data */
    SDL_GamepadDeviceEvent gdevice;         /**< Gamepad device event data */
    SDL_GamepadAxisEvent gaxis;             /**< Gamepad axis event data */
    SDL_GamepadButtonEvent gbutton;         /**< Gamepad button event data */
    SDL_GamepadTouchpadEvent gtouchpad;     /**< Gamepad touchpad event data */
    SDL_GamepadSensorEvent gsensor;         /**< Gamepad sensor event data */
    SDL_AudioDeviceEvent adevice;           /**< Audio device event data */
    SDL_CameraDeviceEvent cdevice;          /**< Camera device event data */
    SDL_SensorEvent sensor;                 /**< Sensor event data */
    SDL_QuitEvent quit;                     /**< Quit request event data */
    SDL_UserEvent user;                     /**< Custom event data */
    SDL_TouchFingerEvent tfinger;           /**< Touch finger event data */
    SDL_PenProximityEvent pproximity;       /**< Pen proximity event data */
    SDL_PenTouchEvent ptouch;               /**< Pen tip touching event data */
    SDL_PenMotionEvent pmotion;             /**< Pen motion event data */
    SDL_PenButtonEvent pbutton;             /**< Pen button event data */
    SDL_PenAxisEvent paxis;                 /**< Pen axis event data */
    SDL_DropEvent drop;                     /**< Drag and drop event data */
    SDL_ClipboardEvent clipboard;           /**< Clipboard event data */

    /* This is necessary for ABI compatibility between Visual C++ and GCC.
       Visual C++ will respect the push pack pragma and use 52 bytes (size of
       SDL_TextEditingEvent, the largest structure for 32-bit and 64-bit
       architectures) for this union, and GCC will use the alignment of the
       largest datatype within the union, which is 8 bytes on 64-bit
       architectures.

       So... we'll add padding to force the size to be the same for both.

       On architectures where pointers are 16 bytes, this needs rounding up to
       the next multiple of 16, 64, and on architectures where pointers are
       even larger the size of SDL_UserEvent will dominate as being 3 pointers.
    */
    Uint8 padding[128];
} SDL_Event;
```

## Remarks

The [SDL_Event](SDL_Event) structure is the core of all event handling in
SDL. [SDL_Event](SDL_Event) is a union of all event structures used in SDL.

## Version

This struct is available since SDL 3.1.3.

## Using events

The [SDL_Event](SDL_Event) structure has two uses:

- Reading events from the event queue
- Placing events on the event queue

## Reading events from the event queue

Reading events from the event queue is done with either [SDL_PollEvent](SDL_PollEvent) or [SDL_PeepEvents](SDL_PeepEvents). We'll use [SDL_PollEvent](SDL_PollEvent) and step through an example.
First off, we create an empty [SDL_Event](SDL_Event) structure.

```c
SDL_Event test_event;
```

[SDL_PollEvent](SDL_PollEvent) removes the next event from the event queue.  If there are no events on the queue it returns 0, otherwise it returns 1. We use a ```while``` loop to process each event in turn.

```c
while (SDL_PollEvent(&test_event)) {
```

The [SDL_PollEvent](SDL_PollEvent) function takes a pointer to an [SDL_Event](SDL_Event) structure that is to be filled with event information. We know that if [SDL_PollEvent](SDL_PollEvent) removes an event from the queue then the event information will be placed in our test_event structure, but we also know that the type of event will be placed in the **type** member of test_event. So to handle each event type separately we use a ```switch``` statement.

```c
  switch (test_event.type) {
```

We need to know what kind of events we're looking for and the event types of those events. So let's assume we want to detect where the user is moving the mouse pointer within our application. We look through our event types and notice that SDL_MOUSEMOTION is, more than likely, the event we're looking for. Looking at the table below tells us that SDL_MOUSEMOTION events are handled within the [SDL_MouseMotionEvent](SDL_MouseMotionEvent) structure which is the **motion** member of [SDL_Event](SDL_Event). We can check for the SDL_MOUSEMOTION event **type** within our ```switch``` statement like so:

```c
    case SDL_MOUSEMOTION:
```

All we need to do now is read the information out of the **motion** member of test_event.

```c
      SDL_Log("We got a motion event.");
      SDL_Log("Current mouse position is: (%d, %d)", test_event.motion.x, test_event.motion.y);
      break;
    default:
      SDL_Log("Unhandled Event!");
      break;
  }
}
SDL_Log("Event queue empty.");
```

## Placing events on the event queue

It is also possible to push events onto the event queue and so use it as a two-way communication path. Both [SDL_PushEvent](SDL_PushEvent) and [SDL_PeepEvents](SDL_PeepEvents) allow you to place events onto the event queue. This is usually used to place a SDL_USEREVENT on the event queue, however you could use it to post fake input events if you wished. Creating your own events is a simple matter of choosing the event type you want, setting the **type** member and filling the appropriate member structure with information.

```c
SDL_Event user_event;
user_event.type = SDL_USEREVENT;
user_event.user.code = 2;
user_event.user.data1 = NULL;
user_event.user.data2 = NULL;
SDL_PushEvent(&user_event);
```

## Relationships between event types and union members

| Event Type                                                                               | Event Structure                                        | SDL_Event Field   |
|------------------------------------------------------------------------------------------|--------------------------------------------------------|-------------------|
| SDL_EVENT_AUDIO_DEVICE_ADDED, SDL_EVENT_AUDIO_DEVICE_REMOVED, etc                        | [SDL_AudioDeviceEvent](SDL_AudioDeviceEvent)           | `adevice`         |
| SDL_EVENT_CAMERA_DEVICE_ADDED, SDL_EVENT_CAMERA_DEVICE_APPROVED, etc                     | [SDL_CameraDeviceEvent](SDL_CameraDeviceEvent)         | `cdevice`         |
| SDL_EVENT_CLIPBOARD_UPDATE                                                               | [SDL_ClipboardEvent](SDL_ClipboardEvent)               | `clipboard`       |
| SDL_EVENT_DISPLAY_ADDED, SDL_EVENT_DISPLAY_REMOVED, etc                                  | [SDL_DisplayEvent](SDL_DisplayEvent)                   | `display`         |
| SDL_EVENT_GAMEPAD_ADDED, SDL_EVENT_GAMEPAD_REMOVED, or SDL_EVENT_GAMEPAD_REMAPPED, etc   | [SDL_GamepadDeviceEvent](SDL_GamepadDeviceEvent)       | `gdevice`         |
| SDL_EVENT_GAMEPAD_AXIS_MOTION                                                            | [SDL_GamepadAxisEvent](SDL_GamepadAxisEvent)           | `gaxis`           |
| SDL_EVENT_GAMEPAD_BUTTON_DOWN, SDL_EVENT_GAMEPAD_BUTTON_UP                               | [SDL_GamepadButtonEvent](SDL_GamepadButtonEvent)       | `gbutton`         |
| SDL_EVENT_GAMEPAD_TOUCHPAD_DOWN, SDL_EVENT_GAMEPAD_TOUCHPAD_MOTION, etc                  | [SDL_GamepadTouchpadEvent](SDL_GamepadTouchpadEvent)   | `gtouchpad`       |
| SDL_EVENT_GAMEPAD_SENSOR_UPDATE                                                          | [SDL_GamepadSensorEvent](SDL_GamepadSensorEvent)       | `gsensor`         |
| SDL_EVENT_DROP_BEGIN, SDL_EVENT_DROP_FILE, SDL_EVENT_DROP_TEXT,  etc                     | [SDL_DropEvent](SDL_DropEvent)                         | `drop`            |
| SDL_EVENT_FINGER_MOTION, SDL_EVENT_FINGER_DOWN, SDL_EVENT_FINGER_UP                      | [SDL_TouchFingerEvent](SDL_TouchFingerEvent)           | `tfinger`         |
| SDL_EVENT_KEYBOARD_ADDED, SDL_EVENT_KEYBOARD_REMOVED                                     | [SDL_KeyboardDeviceEvent(SDL_KeyboardDeviceEvent)      | `kdevice`         |
| SDL_EVENT_KEY_DOWN, SDL_EVENT_KEY_UP                                                     | [SDL_KeyboardEvent](SDL_KeyboardEvent)                 | `key`             |
| SDL_EVENT_JOYSTICK_ADDED, SDL_EVENT_JOYSTICK_REMOVED, SDL_EVENT_JOYSTICK_UPDATE_COMPLETE | [SDL_JoyDeviceEvent](SDL_JoyDeviceEvent)               | `jdevice`         |
| SDL_EVENT_JOYSTICK_AXIS_MOTION                                                           | [SDL_JoyAxisEvent](SDL_JoyAxisEvent)                   | `jaxis`           |
| SDL_EVENT_JOYSTICK_BALL_MOTION                                                           | [SDL_JoyBallEvent](SDL_JoyBallEvent)                   | `jball`           |
| SDL_EVENT_JOYSTICK_HAT_MOTION                                                            | [SDL_JoyHatEvent](SDL_JoyHatEvent)                     | `jhat`            |
| SDL_EVENT_JOYSTICK_BATTERY_UPDATED                                                       | [SDL_JoyBatteryEvent](SDL_JoyBatteryEvent)             | `jbattery`        |
| SDL_EVENT_JOYSTICK_BUTTON_DOWN, SDL_EVENT_JOYSTICK_BUTTON_UP                             | [SDL_JoyButtonEvent](SDL_JoyButtonEvent)               | `jbutton`         |
| SDL_EVENT_MOUSE_ADDED, SDL_EVENT_MOUSE_REMOVED                                           | [SDL_MouseDeviceEvent](SDL_MouseDeviceEvent)           | `mdevice`         |
| SDL_EVENT_MOUSE_MOTION                                                                   | [SDL_MouseMotionEvent](SDL_MouseMotionEvent)           | `motion`          |
| SDL_EVENT_MOUSE_BUTTON_DOWN, SDL_EVENT_MOUSE_BUTTON_UP                                   | [SDL_MouseButtonEvent](SDL_MouseButtonEvent)           | `button`          |
| SDL_EVENT_MOUSE_WHEEL                                                                    | [SDL_MouseWheelEvent](SDL_MouseWheelEvent)             | `wheel`           |
| SDL_EVENT_PEN_PROXIMITY_IN, SDL_EVENT_PEN_PROXIMITY_OUT                                  | [SDL_PenProximityEvent](SDL_PenProximityEvent)         | `pproximity`      |
| SDL_EVENT_PEN_DOWN, SDL_EVENT_PEN_UP                                                     | [SDL_PenTouchEvent](SDL_PenTouchEvent)                 | `ptouch`          |
| SDL_EVENT_PEN_MOTION                                                                     | [SDL_PenMotionEvent](SDL_PenMotionEvent)               | `pmotion`         |
| SDL_EVENT_PEN_BUTTON_DOWN, SDL_EVENT_PEN_BUTTON_UP                                       | [SDL_PenButtonEvent](SDL_PenButtonEvent)               | `pbutton`         |
| SDL_EVENT_PEN_AXIS                                                                       | [SDL_PenAxisEvent](SDL_PenAxisEvent)                   | `paxis`           |
| SDL_EVENT_QUIT                                                                           | [SDL_QuitEvent](SDL_QuitEvent)                         | `quit`            |
| SDL_EVENT_SENSOR_UPDATE                                                                  | [SDL_SensorEvent](SDL_SensorEvent)                     | `sensor`          |
| SDL_EVENT_TEXT_EDITING                                                                   | [SDL_TextEditingEvent](SDL_TextEditingEvent)           | `edit`            |
| SDL_EVENT_TEXT_EDITING_CANDIDATES                                                        | [SDL_TextEditingCandidatesEvent](SDL_TextEditingEvent) | `edit_candidates` |
| SDL_EVENT_TEXT_INPUT                                                                     | [SDL_TextInputEvent](SDL_TextInputEvent)               | `text`            |
| SDL_EVENT_USER                                                                           | [SDL_UserEvent](SDL_UserEvent)                         | `user`            |
| SDL_EVENT_WINDOW_RESIZED, SDL_EVENT_WINDOW_MOVED, etc                                    | [SDL_WindowEvent](SDL_WindowEvent)                     | `window`          |
| Other events                                                                             | [SDL_CommonEvent](SDL_CommonEvent)                     | `common`          |

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

