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

  private:
    char name[SIZE];
    char species[SIZE];
    char breed[SIZE];
    char service[SIZE];
    char misc[SIZE];
};

// Core Functions
void new_animals();
void read_inc(int &count);
int disp_inc();
void edit_inc();
void read_cur();
void updt_cur(int count);
void disp_cur();

// Greetings
void greeting();
void menu_greeting();
void incoming_greeting();
void farewell();

// Utility Functions
int menu();
void call_edit(int count);
void call_menu(int &selection);
char yes_no(const char* str);
void reset_incoming();
void reset_current();
