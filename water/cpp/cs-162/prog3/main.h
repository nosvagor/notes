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
const int MAX {10};      // max number of animals.
const char DLM = '|';   // delimiter used when parsing file

// File Locations
const char CURRENT[] = "src/animals.txt";            // main data file
const char EXAMPLE[] = "src/example_list.txt";   // testing purposes
const char ORIGINAL[] = "src/animals_original.txt";  // used for resetting

// Classes
class animal {
  public:
    animal();
    ~animal();

    void get_info(const char * str, char *& info);
    void read_manual();
    void get_info_auto(char *& info, char dlm, ifstream & in_file);
    void read_auto(ifstream & in_file);
    bool display();
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
    void read_all_auto();
    void read_file_only();
    void display_all();
    void call_edit();
    bool search();

    int animal_count;

  private:
    animal * group;
};

// Utility
int menu();
void get_info(const char * str, char * info);
char yes_no(const char* str);
void call_menu(int &selection);
void edit(animals group);
void update(animals current);
void sleep(int seconds);
void return_to_menu();

// Greetings
void greeting();
void menu_greeting();
void incoming_greeting();
void farewell();
