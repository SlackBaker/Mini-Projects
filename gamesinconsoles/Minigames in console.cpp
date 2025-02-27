#include <iostream>
#include <vector>
#include <string>
#include <random>
using namespace std;

class guessTheNumber {
public:
	int answer;
	void guess() {
		while (true) {
			int randomNum = rand() % 11;

			cout << "To exit write \"0\".Guess the number from 1 to 10:";
			cin >> answer;

			if (answer == 0) {
				cout << "We are turning off the game!" << endl;
				return;
			}

			if (answer == randomNum) {
				cout << "Yes you guessed";
			}
			else {
				cout << "You didn't guess. It was:" << randomNum << endl;
			}
		}	
	}
};

class guessLetter {
public:
	vector<string> letters = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
	string letter;
	void guesslett() {
		while (true) {
			random_device rd;  // Отримання випадкового числа з обладнання
			mt19937 gen(rd()); // Ініціалізація генератора
			uniform_int_distribution<> distr(0, letters.size() - 1); // Визначення діапазону

			// Генерація випадкового індексу та вибір слова
			int randomIndex = distr(gen);
			string randomLetter = letters[randomIndex];

			cout << "Guess the letter. Caps lock only!!! To leave write \"0\"." << endl;

			cin.ignore();
			getline(cin, letter);

			if (letter == randomLetter) {
				cout << "You guessed";
			}
			if (letter == "0") {
				cout << "We are turning off the game!" << endl;
				return;
			}
			else {
				cout << "You didn't guess it was:" << randomLetter << endl;
			}
		}	
	}
};

class TicTacToe {
private:
    vector<vector<char>> board;
    char currentPlayer;

    // Display the game board
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

    // Check if there is a winner
    bool checkWin() {
        // Check rows and columns
        for (int i = 0; i < 3; i++) {
            if ((board[i][0] == currentPlayer && board[i][1] == currentPlayer && board[i][2] == currentPlayer) ||
                (board[0][i] == currentPlayer && board[1][i] == currentPlayer && board[2][i] == currentPlayer)) {
                return true;
            }
        }

        // Check diagonals
        if ((board[0][0] == currentPlayer && board[1][1] == currentPlayer && board[2][2] == currentPlayer) ||
            (board[0][2] == currentPlayer && board[1][1] == currentPlayer && board[2][0] == currentPlayer)) {
            return true;
        }

        return false;
    }

    // Check if the board is full
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
        board = vector<vector<char>>(3, vector<char>(3, ' ')); // Initialize the board with spaces
        currentPlayer = 'X'; // Player X starts
    }

    // Main game loop
    void playGame() {
        cout << "Game: Tic Tac Toe\n";
        displayBoard();

        while (true) {
            int row, col;
            cout << "Player " << currentPlayer << ", enter row and column numbers (1-3): ";
            cin >> row >> col;

            // Validate input
            if (row < 1 || row > 3 || col < 1 || col > 3 || board[row - 1][col - 1] != ' ') {
                cout << "Invalid move. Try again.\n";
                continue;
            }

            // Make the move
            board[row - 1][col - 1] = currentPlayer;
            displayBoard();

            // Check for a win
            if (checkWin()) {
                cout << "Player " << currentPlayer << " wins!\n";
                break;
            }

            // Check for a draw
            if (isDraw()) {
                cout << "It's a draw! The board is full.\n";
                break;
            }

            // Switch player
            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }
    }
};


int main(){
	guessTheNumber guessNumber;
	guessLetter guessletter;
    TicTacToe tictactoe;
	int choose;

	cout << "Choose games:exit[0] random number[1], random letter[2] TicTacToe[3]:";
	cin >> choose;

	switch(choose) {
	case 0:
		return 0;
		break;
	case 1:
			guessNumber.guess();
		break;
	case 2:
		guessletter.guesslett();
		break;
    case 3:
        tictactoe.playGame();
	default:
		cout << "There is no other games like that.";
	}

}