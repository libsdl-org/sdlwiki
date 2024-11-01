###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
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

## Remarks

The [SDL_Event](SDL_Event) structure is the core of all event handling in
SDL. [SDL_Event](SDL_Event) is a union of all event structures used in SDL.

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
      SDL_Log("Current mouse position is: (%d, %d)\n", test_event.motion.x, test_event.motion.y);
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

| Event Type                                                                           | Event Structure                                        | SDL_Event Field |
|--------------------------------------------------------------------------------------|--------------------------------------------------------|-----------------|
| SDL_AUDIODEVICEADDED, SDL_AUDIODEVICEREMOVED                                         | [SDL_AudioDeviceEvent](SDL_AudioDeviceEvent)           | `adevice`       |
| SDL_CONTROLLERAXISMOTION                                                             | [SDL_ControllerAxisEvent](SDL_ControllerAxisEvent)     | `caxis`         |
| SDL_CONTROLLERBUTTONDOWN, SDL_CONTROLLERBUTTONUP                                     | [SDL_ControllerButtonEvent](SDL_ControllerButtonEvent) | `cbutton`       |
| SDL_CONTROLLERDEVICEADDED, SDL_CONTROLLERDEVICEREMOVED, SDL_CONTROLLERDEVICEREMAPPED | [SDL_ControllerDeviceEvent](SDL_ControllerDeviceEvent) | `cdevice`       |
| SDL_DOLLARGESTURE, SDL_DOLLARRECORD                                                  | [SDL_DollarGestureEvent](SDL_DollarGestureEvent)       | `dgesture`      |
| SDL_DROPFILE, SDL_DROPTEXT, SDL_DROPBEGIN, SDL_DROPCOMPLETE                          | [SDL_DropEvent](SDL_DropEvent)                         | `drop`          |
| SDL_FINGERMOTION, SDL_FINGERDOWN, SDL_FINGERUP                                       | [SDL_TouchFingerEvent](SDL_TouchFingerEvent)           | `tfinger`       |
| SDL_KEYDOWN, SDL_KEYUP                                                               | [SDL_KeyboardEvent](SDL_KeyboardEvent)                 | `key`           |
| SDL_JOYAXISMOTION                                                                    | [SDL_JoyAxisEvent](SDL_JoyAxisEvent)                   | `jaxis`         |
| SDL_JOYBALLMOTION                                                                    | [SDL_JoyBallEvent](SDL_JoyBallEvent)                   | `jball`         |
| SDL_JOYHATMOTION                                                                     | [SDL_JoyHatEvent](SDL_JoyHatEvent)                     | `jhat`          |
| SDL_JOYBUTTONDOWN, SDL_JOYBUTTONUP                                                   | [SDL_JoyButtonEvent](SDL_JoyButtonEvent)               | `jbutton`       |
| SDL_JOYDEVICEADDED, SDL_JOYDEVICEREMOVED                                             | [SDL_JoyDeviceEvent](SDL_JoyDeviceEvent)               | `jdevice`       |
| SDL_MOUSEMOTION                                                                      | [SDL_MouseMotionEvent](SDL_MouseMotionEvent)           | `motion`        |
| SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP                                               | [SDL_MouseButtonEvent](SDL_MouseButtonEvent)           | `button`        |
| SDL_MOUSEWHEEL                                                                       | [SDL_MouseWheelEvent](SDL_MouseWheelEvent)             | `wheel`         |
| SDL_MULTIGESTURE                                                                     | [SDL_MultiGestureEvent](SDL_MultiGestureEvent)         | `mgesture`      |
| SDL_QUIT                                                                             | [SDL_QuitEvent](SDL_QuitEvent)                         | `quit`          |
| SDL_SYSWMEVENT                                                                       | [SDL_SysWMEvent](SDL_SysWMEvent)                       | `syswm`         |
| SDL_TEXTEDITING                                                                      | [SDL_TextEditingEvent](SDL_TextEditingEvent)           | `edit`          |
| SDL_TEXTEDITING_EXT                                                                  | [SDL_TextEditingExtEvent](SDL_TextEditingExtEvent)     | `editExt`       |
| SDL_TEXTINPUT                                                                        | [SDL_TextInputEvent](SDL_TextInputEvent)               | `text`          |
| SDL_USEREVENT                                                                        | [SDL_UserEvent](SDL_UserEvent)                         | `user`          |
| SDL_WINDOWEVENT                                                                      | [SDL_WindowEvent](SDL_WindowEvent)                     | `window`        |
| Other events                                                                         | [SDL_CommonEvent](SDL_CommonEvent)                     | `common`        |

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryEvents](CategoryEvents)

