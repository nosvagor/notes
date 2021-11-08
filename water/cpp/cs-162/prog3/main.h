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
const int MAX {3};     // max number of animals.
const char DLM = '|';   // delimiter used when parsing file

// File Locations
const char CURRENT[] = "src/animals.txt";            // main data file
const char ORIGINAL[] = "src/animals_original.txt";  // used for resetting

// Classes
class animal {
  public:
    animal();
    ~animal();

    void get_info(const char * str, char *& info);
    void read();
    void display();
    void edit();
    bool compare();

  private:
    char * name;
    char * species;
    char * breed;
    char * service;
    char * misc;
};

class animals {
  public:
    animals();
    ~animals();

    void read_all();
    void display_all();
    void call_edit();
    bool search();

  private:
    animal * group;
    int animal_count;
};

// Utility
int menu();
void get_info(const char * str, char * info);
char yes_no(const char* str);
void call_menu(int &selection);
void edit_update();
void sleep(int seconds);

// Greetings
void greeting();
void menu_greeting();
void incoming_greeting();
void farewell();
