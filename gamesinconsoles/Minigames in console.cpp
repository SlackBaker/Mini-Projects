#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <map>
#include <ctime>
#include <cstdlib>
#include <windows.h>

using namespace std;

void SetColor(int text, int background = 0) {
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, text + (background << 4));
}

class guessTheNumber {
public:
    int answer;
    void guess() {
        while (true) {
            int randomNum = rand() % 11;

            cout << "To exit write \"0\". Guess the number from 1 to 10: ";
            cin >> answer;

            if (answer == 0) {
                cout << "We are turning off the game!" << endl;
                return;
            }

            if (answer == randomNum) {
                cout << "Yes you guessed!\n";
            }
            else {
                cout << "You didn't guess. It was: " << randomNum << endl;
            }
        }
    }
};

class guessLetter {
public:
    vector<string> letters = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
    string letter;
    void guesslett() {
        while (true) {
            random_device rd;
            mt19937 gen(rd());
            uniform_int_distribution<> distr(0, letters.size() - 1);

            int randomIndex = distr(gen);
            string randomLetter = letters[randomIndex];

            cout << "Guess the letter. Caps lock only!!! To leave write \"0\"." << endl;
            cin >> letter;

            if (letter == "0") {
                cout << "We are turning off the game!" << endl;
                return;
            }

            if (letter == randomLetter) {
                cout << "You guessed!\n";
            }
            else {
                cout << "You didn't guess. It was: " << randomLetter << endl;
            }
        }
    }
};

class TicTacToe {
private:
    vector<vector<char>> board;
    char currentPlayer;

    void displayBoard() {
        cout << "\n";
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cout << board[i][j];
                if (j < 2) cout << " | ";
            }
            cout << "\n";
            if (i < 2) cout << "--+---+--\n";
        }
        cout << "\n";
    }

    bool checkWin() {
        for (int i = 0; i < 3; i++) {
            if ((board[i][0] == currentPlayer && board[i][1] == currentPlayer && board[i][2] == currentPlayer) ||
                (board[0][i] == currentPlayer && board[1][i] == currentPlayer && board[2][i] == currentPlayer)) {
                return true;
            }
        }

        if ((board[0][0] == currentPlayer && board[1][1] == currentPlayer && board[2][2] == currentPlayer) ||
            (board[0][2] == currentPlayer && board[1][1] == currentPlayer && board[2][0] == currentPlayer)) {
            return true;
        }

        return false;
    }

    bool isDraw() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }

public:
    TicTacToe() {
        board = vector<vector<char>>(3, vector<char>(3, ' '));
        currentPlayer = 'X';
    }

    void playGame() {
        cout << "Game: Tic Tac Toe\n";
        displayBoard();

        while (true) {
            int row, col;
            cout << "Player " << currentPlayer << ", enter row and column numbers (1-3): ";
            cin >> row >> col;

            if (row < 1 || row > 3 || col < 1 || col > 3 || board[row - 1][col - 1] != ' ') {
                cout << "Invalid move. Try again.\n";
                continue;
            }

            board[row - 1][col - 1] = currentPlayer;
            displayBoard();

            if (checkWin()) {
                cout << "Player " << currentPlayer << " wins!\n";
                break;
            }

            if (isDraw()) {
                cout << "It's a draw! The board is full.\n";
                break;
            }

            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }
    }
};

class GuessWords {
public:
    vector<string> animals = { "Cat", "Dog", "Chicken", "Frog", "Wolf" };
    vector<string> fruits = { "Apple", "Banana", "Cherry", "Grape", "Orange" };

    void PlayGame() {
        string topic;
        cout << "Choose topic: fruits, animals\n";
        cin.ignore();
        getline(cin, topic);

        vector<string> words;

        if (topic == "animals") {
            words = animals;
        }
        else if (topic == "fruits") {
            words = fruits;
        }
        else {
            cout << "Invalid topic.\n";
            return;
        }

        srand(time(0));
        string word = words[rand() % words.size()];
        string guessedWord(word.size(), '_');
        int attempts = 6;

        cout << "Try to guess the word!\n";

        while (attempts > 0) {
            cout << "Word: " << guessedWord << " (Attempts left: " << attempts << ")\n";
            cout << "Enter a letter: ";
            char guess;
            cin >> guess;

            bool found = false;
            for (size_t i = 0; i < word.size(); i++) {
                if (tolower(word[i]) == tolower(guess)) {
                    guessedWord[i] = word[i];
                    found = true;
                }
            }

            if (!found) {
                attempts--;
                cout << "Wrong guess!\n";
            }

            if (guessedWord == word) {
                cout << "Congratulations! You guessed the word: " << word << endl;
                return;
            }
        }

        cout << "Game over! The word was: " << word << endl;
    }
};

class Charlie {
public:
    void Ask() {

    }
};

int main() {
    guessTheNumber guessNumber;
    guessLetter guessletter;
    TicTacToe tictactoe;
    GuessWords guessword;
    Charlie charlie;
    int choose;

    cout << "Choose games: exit[0], ";
    SetColor(2);
    cout << "random number[1], ";
    SetColor(3);
    cout << "random letter[2], ";
    SetColor(4);
    cout << "TicTacToe[3], ";
    SetColor(5);
    cout << "Guess a word[4]: ";
    SetColor(7);
    cin >> choose;

    switch (choose) {
    case 0:
        return 0;
    case 1:
        guessNumber.guess();
        break;
    case 2:
        guessletter.guesslett();
        break;
    case 3:
        tictactoe.playGame();
        break;
    case 4:
        guessword.PlayGame();
        break;
    default:
        cout << "There is no other games like that.\n";
    }
}
