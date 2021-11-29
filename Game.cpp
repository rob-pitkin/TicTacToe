#include "Game.hpp"

Game::Game()
{
    board = std::make_shared<std::vector<int>>();
    for (int i = 0; i < 9; i++)
    {
        board->push_back(0);
    }
}

void Game::makeMove(int row, int col, int player)
{
    if (row > 2 || row < 0 || col < 0 || col > 2 || player < 1 || player > 2)
    {
        std::cout << "Bad Input!" << endl;
        return;
    }
    if (board->at(row*3+col) == 0)
    {
        board->at(row*3+col) = player;
    }
    else
    {
        std::cout << "Spot already filled!" << std::endl;
    }
    return;
}

bool Game::winCondition(int player)
{
    return false;
}

void Game::printBoard()
{
    std::cout << "-------------" << std::endl;
    for (int i = 0; i < 3; i++)
    {
        std::cout << "|";
        for (int j = 0; j < 3; j++)
        {
            int currIndex = i*3 + j;
            if (board->at(currIndex) == 1)
            {
                std::cout << " X |";
            }
            else if (board->at(currIndex) == 2)
            {
                std::cout << " O |";
            }
            else
            {
                std::cout << "   |";
            }
        }
        std::cout << "\n-------------" << std::endl;
    }
}
