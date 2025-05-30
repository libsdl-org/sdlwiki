#include <SDL2/SDL.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Definiamo alcune costanti
#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600
#define PLAYER_SPEED 5
#define BULLET_SPEED 10
#define ENEMY_SPEED 3
#define MAX_BULLETS 5
#define MAX_ENEMIES 10

// Strutture per il giocatore, le pallottole e i nemici
typedef struct {
    int x, y;
    SDL_Rect rect;
    SDL_Texture *texture;
} Player;

typedef struct {
    int x, y;
    SDL_Rect rect;
    SDL_Texture *texture;
} Bullet;

typedef struct {
    int x, y;
    SDL_Rect rect;
    SDL_Texture *texture;
} Enemy;

// Funzione per inizializzare SDL
bool init(SDL_Window **window, SDL_Renderer **renderer) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("SDL non può essere inizializzato! SDL_Error: %s\n", SDL_GetError());
        return false;
    }

    *window = SDL_CreateWindow("Space Shooter", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    if (!*window) {
        printf("Finestra non può essere creata! SDL_Error: %s\n", SDL_GetError());
        return false;
    }

    *renderer = SDL_CreateRenderer(*window, -1, SDL_RENDERER_ACCELERATED);
    if (!*renderer) {
        printf("Renderer non può essere creato! SDL_Error: %s\n", SDL_GetError());
        return false;
    }

    return true;
}

// Funzione per caricare texture
SDL_Texture* loadTexture(SDL_Renderer *renderer, const char *path) {
    SDL_Texture *texture = NULL;
    texture = SDL_CreateTextureFromSurface(renderer, SDL_LoadBMP(path));
    if (!texture) {
        printf("Impossibile caricare l'immagine! SDL_Error: %s\n", SDL_GetError());
    }
    return texture;
}

// Funzione per gestire il movimento del giocatore
void handlePlayerMovement(SDL_Event *e, Player *player) {
    if (e->type == SDL_KEYDOWN) {
        switch (e->key.keysym.sym) {
            case SDLK_LEFT:
                if (player->x > 0) player->x -= PLAYER_SPEED;
                break;
            case SDLK_RIGHT:
                if (player->x < SCREEN_WIDTH - player->rect.w) player->x += PLAYER_SPEED;
                break;
            case SDLK_UP:
                if (player->y > 0) player->y -= PLAYER_SPEED;
                break;
            case SDLK_DOWN:
                if (player->y < SCREEN_HEIGHT - player->rect.h) player->y += PLAYER_SPEED;
                break;
        }
    }
    player->rect.x = player->x;
    player->rect.y = player->y;
}

// Funzione per aggiornare le pallottole
void updateBullets(Bullet bullets[], int *bulletCount) {
    for (int i = 0; i < *bulletCount; i++) {
        bullets[i].y -= BULLET_SPEED;
        if (bullets[i].y < 0) {
            // Rimuovi le pallottole fuori schermo
            bullets[i] = bullets[*bulletCount - 1];
            (*bulletCount)--;
        }
    }
}

// Funzione per gestire i nemici
void updateEnemies(Enemy enemies[], int *enemyCount) {
    for (int i = 0; i < *enemyCount; i++) {
        enemies[i].y += ENEMY_SPEED;
        if (enemies[i].y > SCREEN_HEIGHT) {
            enemies[i] = enemies[*enemyCount - 1];
            (*enemyCount)--;
        }
    }
}

// Funzione per controllare le collisioni tra pallottole e nemici
void checkCollisions(Bullet bullets[], int *bulletCount, Enemy enemies[], int *enemyCount) {
    for (int i = 0; i < *bulletCount; i++) {
        for (int j = 0; j < *enemyCount; j++) {
            if (SDL_HasIntersection(&bullets[i].rect, &enemies[j].rect)) {
                // Distruggi il nemico e la pallottola
                bullets[i] = bullets[*bulletCount - 1];
                (*bulletCount)--;

                enemies[j] = enemies[*enemyCount - 1];
                (*enemyCount)--;

                // Aggiungi un nuovo nemico (per semplicità)
                enemies[*enemyCount].x = rand() % (SCREEN_WIDTH - 50);
                enemies[*enemyCount].y = 0;
                enemies[*enemyCount].rect.x = enemies[*enemyCount].x;
                enemies[*enemyCount].rect.y = enemies[*enemyCount].y;
                (*enemyCount)++;
            }
        }
    }
}

// Funzione per gestire gli input
void handleInput(SDL_Event *e, bool *quit, Player *player, Bullet bullets[], int *bulletCount) {
    while (SDL_PollEvent(e)) {
        if (e->type == SDL_QUIT) {
            *quit = true;
        }
        handlePlayerMovement(e, player);

        if (e->type == SDL_KEYDOWN && e->key.keysym.sym == SDLK_SPACE && *bulletCount < MAX_BULLETS) {
            // Spara una pallottola
            bullets[*bulletCount].x = player->x + player->rect.w / 2 - 5;
            bullets[*bulletCount].y = player->y;
            bullets[*bulletCount].rect = (SDL_Rect){bullets[*bulletCount].x, bullets[*bulletCount].y, 10, 20};
            (*bulletCount)++;
        }
    }
}

// Funzione per disegnare gli oggetti
void render(SDL_Renderer *renderer, Player *player, Bullet bullets[], int bulletCount, Enemy enemies[], int enemyCount) {
    SDL_RenderClear(renderer);

    // Disegna il giocatore
    SDL_RenderCopy(renderer, player->texture, NULL, &player->rect);

    // Disegna le pallottole
    for (int i = 0; i < bulletCount; i++) {
        SDL_RenderCopy(renderer, bullets[i].texture, NULL, &bullets[i].rect);
    }

    // Disegna i nemici
    for (int i = 0; i < enemyCount; i++) {
        SDL_RenderCopy(renderer, enemies[i].texture, NULL, &enemies[i].rect);
    }

    SDL_RenderPresent(renderer);
}

int main() {
    SDL_Window *window = NULL;
    SDL_Renderer *renderer = NULL;
    SDL_Event e;

    // Inizializzazione
    if (!init(&window, &renderer)) {
        printf("Errore di inizializzazione!\n");
        return 1;
    }

    // Carica le texture
    SDL_Texture *playerTexture = loadTexture(renderer, "player.bmp");
    SDL_Texture *bulletTexture = loadTexture(renderer, "bullet.bmp");
    SDL_Texture *enemyTexture = loadTexture(renderer, "enemy.bmp");

    // Inizializza il giocatore
    Player player = {SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50, {SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50, 50, 50}, playerTexture};
