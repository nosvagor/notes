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
const int MAX {10};     // max number of animals.
const char DLM = '|';   // delimiter used when parsing/writing to external file.

// File Locations
const char CURRENT[] = "src/animals.txt";            // main data file
const char EXAMPLE[] = "src/example_list.txt";       // example external file
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
    void update(int animal_count);
    bool compare(char * match, const char * info);

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
    bool call_update();
    void call_compare(const char * info);

    int animal_count;

  private:
    animal * group;
};

// Utility
int menu();
char yes_no(const char * str);
void sleep(int seconds);
void return_to_menu();
void file_reset();

// Greetings
void greeting();
void menu_greeting();
void incoming_greeting();
void farewell();
