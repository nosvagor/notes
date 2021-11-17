// ╦ ╦┌─┐┌─┐┌┬┐┌─┐┬─┐
// ╠═╣├┤ ├─┤ ││├┤ ├┬┘
// ╩ ╩└─┘┴ ┴─┴┘└─┘┴└─
// cullyn --- cs162 --- program 4
// Purpose: this is the main header file which consists of:
// #includes, constants, class declarations, and function prototypes

// INCLUDES
#include <cctype>
#include <cstring>
#include <fstream>
#include <iostream>
#include <chrono>
#include <thread>
using namespace std;

// CONSTANTS
const int SIZE {69};    // standard input size.
const char DLM = '|';   // delimiter used when reading/writing external files.

// EXTERNAL FILE PATHS
const char CURRENT[] = "src/current.txt";       // main data file
const char EXAMPLE[] = "src/example.txt";       // example external file
const char ORIGINAL[] = "src/original.txt";     // used for resetting

// CLASSES
class entry {
  public:
    entry();
    ~entry();

    void read_manual();
    void read_auto(ifstream & in_file);

    void display();
    void edit();
    bool compare();

    void write();

  private:
    char * name;
    char * description;
    char * example;
    int  difficulty;
    bool used;
};

struct node {
  entry data;
  node * next;
};

class list {
  public:
    list();
    ~list();

    void build();

    void display_all();
    bool search();
    bool edit();
    void sort();

    void save();

  private:
   node *head;
   node *tail;
};

// UTILITY FUNCTIONS
int menu();
char yes_no(const char * str);
void sleep(int ms);
void return_to_menu();
void file_reset();

// GREETINGS
void greeting();
void menu_greeting();
void farewell();
