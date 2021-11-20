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
  used = false;
  difficulty = 0;
}

// destructor
entry::~entry() {
  if (name) delete [] name;
  if (description) delete [] description;
  if (example) delete [] example;
  used = false;
  difficulty = 0;
}
//===========================================================================//


//===========================================================================//
void entry::read_manual() {
  auto get_input = [](const char * str, char *& member) {
    char temp[SIZE];

    do {
      cout << str;
      cin.get(temp, SIZE, '\n');
      cin.clear();
      cin.ignore(SIZE, '\n');
    } while (!temp[0]);

    member = new char [strlen(temp) + 1];
    strcpy(*& member, temp);
    if (!temp[0]) memset(temp, 0, SIZE);
  };

  get_input("Syntax name: ", name);
  get_input("description: ", description);
  get_input("example: ", example);

  used = yes_no("Have you used this syntax?");

  if (!used) {
    difficulty = 0;
    return;
  }

  do {
    cout << "Difficulty [1--5]: ";
    cin >> difficulty;
    cin.clear();
    cin.ignore(420, '\n');
  } while (difficulty < 0 || difficulty > 5);
}

void entry::read_auto(ifstream & in_file) {

}



void entry::display() {

  if (!name) return;

  cout << "\nName: " << name
       << "\n  - Description: " << description
       << "\n  - Example: " << example
       << "\n  - Used?: " << used
       << "\n  - Difficulty: " << difficulty
       << endl;
}



void entry::edit() {

}



bool entry::compare() {
  return false;
}

void write();
//===========================================================================//
