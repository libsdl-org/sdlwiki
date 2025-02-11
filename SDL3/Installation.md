#include <SDL2/SDL.h>
#include <iostream>

// Инициализация SDL и аудиосистемы
bool init() {
    if (SDL_Init(SDL_INIT_AUDIO) < 0) {
        std::cerr << "SDL could not initialize! SDL Error: " << SDL_GetError() << std::endl;
        return false;
    }
    return true;
}

// Загрузка и воспроизведение звукового файла
bool playSound(const char* file) {
    if (SDL_LoadWAV(file, &wavSpec, &wavBuffer, &wavLength) == nullptr) {
        std::cerr << "Error: Could not load the sound file. SDL Error: " << SDL_GetError() << std::endl;
        return false;
    }

    // Устанавливаем аудиоспецификацию и воспроизводим звук
    SDL_AudioSpec wavSpec;
    Uint32 wavLength;
    Uint8 *wavBuffer;

    SDL_AudioDeviceID deviceId = SDL_OpenAudioDevice(nullptr, 0, &wavSpec, nullptr, 0);
    if (deviceId == 0) {
        std::cerr << "Error: Could not open audio device. SDL Error: " << SDL_GetError() << std::endl;
        SDL_FreeWAV(wavBuffer);
        return false;
    }

    SDL_QueueAudio(deviceId, wavBuffer, wavLength);
    SDL_PauseAudioDevice(deviceId, 0);

    // Ждем, пока звук закончится
    SDL_Delay((wavLength / wavSpec.freq) * 1000);

    SDL_CloseAudioDevice(deviceId);
    SDL_FreeWAV(wavBuffer);

    return true;
}

int main() {
    if (!init()) {
        return 1;
    }

    if (!playSound("Миндаль-Покажи-ай.wav")) {
        return 1;
    }

    SDL_Quit();
    return 0;
}
