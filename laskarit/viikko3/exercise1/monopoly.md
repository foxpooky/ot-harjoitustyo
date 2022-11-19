```mermaid
  classDiagram
    Game "1" --> "2" Die
    Game "1" --> "2-8" Player
    Game "1" --> "1" Board
    Board "1" --> "40" Tile
    Tile "1" --> "1" Tile
    Player "1" --> "1" Pawn
    Pawn "1" --> "1" Tile

    class Game
    class Board
    class Tile
    class Player
    class Pawn
    class Die

```