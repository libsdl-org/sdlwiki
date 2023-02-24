# Event Handling

'''Include File(s):'''  [http://hg.libsdl.org/SDL/file/default/include/SDL_events.h SDL_events.h]


## Introduction
Event handling allows your application to receive input from the user. Event handling is initialized (along with video) with a call to:

<syntaxhighlight lang='c'>
SDL_Init(SDL_INIT_VIDEO);
</syntaxhighlight>

 (''see'' [[CategoryInit|Initialization & Shutdown]] and [[SDL_Init]]() ''for details'')

Internally, SDL stores all the events waiting to be handled in an event queue.  Using functions like [[SDL_PollEvent]](), [[SDL_PeepEvents]]() and [[SDL_WaitEvent]]() you can observe and handle waiting input events.

The event queue itself is composed of a series of [[SDL_Event]] structures, one for each waiting event. [[SDL_Event]] structures are read from the queue with the [[SDL_PollEvent]]() function and it is then up to the application to process the information stored with them.

## Enumerations
<<FullSearchCached(category:CategoryEvents -category:CategoryStruct -category:CategoryAPI -title:SGEnumerations)>>

## Structures
<<FullSearchCached(category:CategoryEvents -category:CategoryEnum -category:CategoryAPI -title:SGStructures)>>

## Functions
<<FullSearchCached(category:CategoryEvents -category:CategoryEnum -category:CategoryStruct -title:SGFunctions)>>

<!-- BEGIN CATEGORY LIST -->
- [SDL_AudioDeviceEvent](SDL_AudioDeviceEvent)
- [SDL_ControllerAxisEvent](SDL_ControllerAxisEvent)
- [SDL_ControllerButtonEvent](SDL_ControllerButtonEvent)
- [SDL_ControllerDeviceEvent](SDL_ControllerDeviceEvent)
- [SDL_DisplayEventID](SDL_DisplayEventID)
- [SDL_DropEvent](SDL_DropEvent)
- [SDL_Event](SDL_Event)
- [SDL_EventFilter](SDL_EventFilter)
- [SDL_EventState](SDL_EventState)
- [SDL_EventType](SDL_EventType)
- [SDL_Finger](SDL_Finger)
- [SDL_GetEventState](SDL_GetEventState)
- [SDL_JoyAxisEvent](SDL_JoyAxisEvent)
- [SDL_JoyButtonEvent](SDL_JoyButtonEvent)
- [SDL_JoyDeviceEvent](SDL_JoyDeviceEvent)
- [SDL_JoyHatEvent](SDL_JoyHatEvent)
- [SDL_KeyboardEvent](SDL_KeyboardEvent)
- [SDL_MouseButtonEvent](SDL_MouseButtonEvent)
- [SDL_MouseMotionEvent](SDL_MouseMotionEvent)
- [SDL_MouseWheelEvent](SDL_MouseWheelEvent)
- [SDL_QuitEvent](SDL_QuitEvent)
- [SDL_QuitRequested](SDL_QuitRequested)
- [SDL_SensorEvent](SDL_SensorEvent)
- [SDL_SysWMEvent](SDL_SysWMEvent)
- [SDL_TextEditingEvent](SDL_TextEditingEvent)
- [SDL_TextInputEvent](SDL_TextInputEvent)
- [SDL_TouchFingerEvent](SDL_TouchFingerEvent)
- [SDL_UserEvent](SDL_UserEvent)
- [SDL_WindowEvent](SDL_WindowEvent)
- [SDL_WindowEventID](SDL_WindowEventID)
<!-- END CATEGORY LIST -->

----
[[CategoryCategory]]
