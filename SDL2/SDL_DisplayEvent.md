# SDL_DisplayEvent 
A structure that contains display state change event data

## Data Fields 

|        |           |                             |
|--------|-----------|-----------------------------|
| Uint32 | **type**      | SDL_DISPLAYEVENT            |
| Uint32 | **timestamp** | Timestamp in milliseconds   |
| Uint32 | **display**   | The associated display index|
| Uint8  | **event**     | [SDL_DisplayEventID](https://wiki.libsdl.org/SDL_DisplayEventID) |
| Sint32 | **data1** | Event associated data|

## Code Examples
```c++
SDL_Event ev;
    
while (SDL_PollEvent(&ev) != 0) {
    if (ev.type == SDL_DISPLAYEVENT) {
        switch (ev.display.event) {
            case SDL_DISPLAYEVENT_CONNECTED:
                SDL_Log("A new display with id %d was connected", ev.display.display);
                break;
            case SDL_DISPLAYEVENT_DISCONNECTED:
                SDL_Log("The display with id %d was disconnected", ev.display.display);
                break;
            case SDL_DISPLAYEVENT_ORIENTATION:
                SDL_Log("The orientation of display with id %d was changed", ev.display.display);
                break;
        }
    }
}
```

## Remarks
[SDL_DisplayEvent](https://wiki.libsdl.org/SDL_DisplayEvent) is a member of the [SDL_Event](https://wiki.libsdl.org/SDL_Event) union and is used when an event of type SDL_DISPLAYEVENT is reported.  You would access it through the event's <code>display</code> field.

----
[CategoryStruct](CategoryStruct), [CategoryEvents](CategoryEvents)

