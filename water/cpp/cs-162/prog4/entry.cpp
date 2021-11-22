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
    cout << "Difficulty [1--10]: ";
    cin >> difficulty;
    cin.clear();
    cin.ignore(420, '\n');
  } while (!(difficulty > 0 && difficulty <= 10));
}

void entry::read_auto(ifstream & in_file) {

  auto read_line = [](char *& member, ifstream & in_file) {
    char temp[SIZE];

    in_file.get(temp, SIZE, DLM);
    in_file.ignore(SIZE, DLM);
    if (!strlen(temp)) return;

    member = new char [strlen(temp) + 1];
    strcpy(member, temp);
  };

  read_line(name, in_file);
  read_line(description, in_file);
  read_line(example, in_file);

  char temp[2];
  in_file.get(temp, 2, DLM);
  in_file.ignore(SIZE, DLM);
  used = ((temp[0] - '0') != 0) ? true : false;

  in_file.get(temp, 2, '\n');
  in_file.ignore(SIZE, '\n');
  difficulty = temp[0] - '0';
}



void entry::display() {

  if (!name) return;
  const char * used_str = used ? "true" : "false";

  cout << "\nName: " << name
       << "\n  - Description: " << description
       << "\n  - Example: " << example
       << "\n  - Used?: " << used_str
       << " ==> difficulty [1--10]: " << difficulty
       << endl;
}

void entry::write() {
    ofstream out_file;
    out_file.open(CURRENT, ios::app);

    out_file
      << name << DLM
      << description << DLM
      << example << DLM
      << used << DLM
      << difficulty << endl;

    out_file.close();
    out_file.clear();
}



bool entry::compare(char query[SIZE], int search_select) {

  bool result = false;

  switch (search_select) {
    case 1: // name
      if (!strcmp(query, name))
        result = true;
      break;

    case 2: // difficulty
      if (query[0] + query[1] - '0' == difficulty)
        result = true;
      break;
  }

  return result;
}
//===========================================================================//
