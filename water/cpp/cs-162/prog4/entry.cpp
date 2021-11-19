// ┌─┐┌┐┌┌┬┐┬─┐┬ ┬
// ├┤ │││ │ ├┬┘└┬┘
// └─┘┘└┘ ┴ ┴└─ ┴
// cullyn --- cs162 --- program 4
// Purpose: this file implements the class entry methods, used for manipulation
// of each specific syntax entry.

//===========================================================================//
  #include "header.h"
//===========================================================================//


//===========================================================================//
// constructor
entry::entry() {
  name = NULL;
  description = NULL;
  example = NULL;
  difficulty = 0;
  used = false;
}

// destructor
entry::~entry() {
  if (name) delete [] name;
  if (description) delete [] description;
  if (example) delete [] example;
  difficulty = 0;
  used = false;
}
//===========================================================================//


//===========================================================================//
void entry::read_manual() {

  auto get_input = [&](const char * str, auto member) {
    char temp[SIZE];

    while (!temp[0] && typeid(member) == typeid(char)) {
      cout << str;
      cin.get(temp, SIZE, '\n');
      cin.clear();
      cin.ignore(SIZE, '\n');
    }

    strcpy(member, temp);

    if (typeid(member) == typeid(int)) {
      cout << str;
      cin.get(member, SIZE, '\n');
      cin.ignore(SIZE, '\n');
    }

    if (typeid(member) == typeid(bool)) {
      (yes_no(str) == 'y') ? member = true : member = false;
    }
  };

  cout << endl;
  get_input("Syntax name: ", name);
}

void read_auto(ifstream & in_file);

void display();
void edit();
bool compare();

void write();
//===========================================================================//
