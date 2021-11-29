#ifndef GAME_HPP_
#define GAME_HPP_

#include <iostream>
#include <memory>
#include <vector>

class Game
{
public:
    Game();
    void makeMove(int row, int col, int player);
    bool winCondition(int player);
    void printBoard();
private:
    std::shared_ptr<std::vector<int>> board;
};

#endif