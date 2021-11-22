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
const int SIZE {128};   // standard input size.
const char DLM = '|';   // delimiter used when reading/writing external files.

// EXTERNAL FILE PATHS
const char CURRENT[] = "src/current.txt";       // main data file
const char EXAMPLE[] = "src/example.txt";       // example external file
const char ORIGINAL[] = "src/original.txt";     // used for resetting

// STRUCTS & CLASSES
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
    bool used;
    int  difficulty;
};

struct node {
  entry data;
  node * next;
};

class list {
  public:
    list();
    void build(node *& head, node *& tail, ifstream & in_file);
    void destroy(node *& head);
    ~list();

    void insert(node *& head);
    void display_all(node *& head);
    bool search(node *& head);
    bool edit(node *& head);
    void sort(node *& head);

    node *head;
    node *tail;

  private:
    // might move some nodes and functions to private
};

// UTILITY FUNCTIONS
int menu();
bool yes_no(const char * str);
void return_to_menu();
void save(node *& head);
void file_reset();

// GREETINGS
void greeting();
void menu_greeting();
void farewell();
