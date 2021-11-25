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
// get_input is not an entry function per se, but it is used to get dynamically
// allocated arrays in cases of manual input.
void get_input (const char * str, char *& member) {
  char temp[SIZE];

  do {
    cout << str;
    cin.get(temp, SIZE, '\n');
    cin.clear();
    cin.ignore(SIZE, '\n');
  } while (!temp[0]);

  member = new char [strlen(temp) + 1];
  strcpy(*& member, temp);
}


// wrapper function for manual input, self explanatory.
void entry::read_manual() {

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


// updates entry with data from external file, assumes all data in external
// file is in valid format.
void entry::read_auto(ifstream & in_file) {

  // read_line is the automatic version of get_input, used for creating
  // dynamically allocated arrays when reading from external file.
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

  char temp[2]; // temp array for chars for input of used and difficulty data.

  in_file.get(temp, 2, DLM);
  in_file.ignore(SIZE, DLM);
  used = ((temp[0] - '0') != 0) ? true : false; // convert input to boolean.

  in_file.get(temp, 2, '\n');
  in_file.ignore(SIZE, '\n');
  difficulty = temp[0] - '0'; // convert input to int
}


// display... Displays  the data...
void entry::display() {

  // if name is empty, then entire entry is empty.
  if (!name) return;

  const char * used_str = used ? "true" : "false"; // convert boolean to string.

  cout << "\nName: " << name
       << "\n  - Description: " << description
       << "\n  - Example: " << example
       << "\n  - Used?: " << used_str
       << " ==> difficulty [1--10]: " << difficulty
       << endl;
}


// write... Writes the data contained in entries objects to an external file.
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



// compare.. Compares a query with data member, given a selection option from
// switch menu selector. Can easily be expanded for comparable fields.
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


// edit... Edits the selected entry. Original data is not maintained, and new
// entry simply overwrites current data.
void entry::edit() {

  int edit_select = {0}; // selection repose variable.

  edit_select = menu(1,5,3); // edit search menu.

 switch (edit_select) {
    case 1:
      get_input("Syntax name: ", name);
      break;

    case 2:
      get_input("New description: ", description);
      break;

    case 3:
      get_input("Example: ", example);
      break;

    case 4:
      used = yes_no("Used?");
      break;

    case 5:
      do {
        cout << "Difficulty [1--10]: ";
        cin >> difficulty;
        cin.clear();
        cin.ignore(420, '\n');
      } while (!(difficulty > 0 && difficulty <= 10));
      break;
 }

}
//===========================================================================//
