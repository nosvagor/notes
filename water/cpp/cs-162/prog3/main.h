// ╔╦╗┌─┐┬┌┐┌  ╦ ╦┌─┐┌─┐┌┬┐┌─┐┬─┐
// ║║║├─┤││││  ╠═╣├┤ ├─┤ ││├┤ ├┬┘
// ╩ ╩┴ ┴┴┘└┘  ╩ ╩└─┘┴ ┴─┴┘└─┘┴└─
// cullyn --- cs162
// Purpose: this is the main header file which consists of:
// includes, constants, class interfaces, and prototypes

// Includes
#include <cctype>
#include <cstring>
#include <fstream>
#include <iostream>
#include <chrono>
#include <thread>
using namespace std;

// Constants
const int SIZE {69};    // standard input array size.
const int INC {5};      // max number of animals support for manual input.
const int CUR {10};     // max number of animals on farm.
const char DLM = '|';   // delimiter used when parsing file

// File Locations
const char CURRENT[] = "src/animals.txt";            // main data file
const char ORIGINAL[] = "src/animals_original.txt";  // used for resetting

// Classes
class animal {
  public:
    animal();
    void read();
    void display();
    void edit();

  private:
    char name[SIZE];
    char species[SIZE];
    char breed[SIZE];
    char service[SIZE];
    char misc[SIZE];
};

// Core Functions
void read();
void display();
void edit();
void update();
void search();
void reset();

int menu();
char yes_no(const char* str);
void call_menu(int &selection);
void edit_update();

// Greetings
void greeting();
void menu_greeting();
void incoming_greeting();
void farewell();
