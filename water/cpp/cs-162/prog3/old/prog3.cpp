// ┌─┐┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ┌┬┐┬ ┬┬─┐┌─┐┌─┐
// ├─┘├┬┘│ ││ ┬├┬┘├─┤│││   │ ├─┤├┬┘├┤ ├┤
// ┴  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴   ┴ ┴ ┴┴└─└─┘└─┘
// cullyn newman -- cs162

// Meta-purpose: further practice using arrays of characters, but now with the
// inclusion of structures, data files, and classes.

// Program-purpose: maintain a list of animals that can perform service
// activities. Data will be organized by breed, species, service,
// compatibility, and specific (special) information that relates to each
// animal in question.
// --
// This program utilizes an external file called animal.txt that will be read
// and written to. New input taken from the user will be appended to existing
// data in file. The user will have the option to supply a different source
// file if desired instead of inputting new data.


#include <cctype>
#include <cstring>
#include <fstream>
#include <iostream>
#include <chrono>
#include <thread>
using namespace std;

// Constants
const int N {69};       // default array size.
const int MAX {5};  // max number of animals support for manual input.
const int MAX_CUR {10}; // max number of animals on farm.
const char DLM = '|';   // delimiter used when parsing file

const char *CUR_ANIMALS = "../src/animals.txt";            // main data file
const char *ORIG_ANIMALS = "../src/animals_original.txt";  // used for resetting

// Structure
struct animal {
  char name[N];     // custom field, name of animal.
  char species[N];  // animal species.
  char breed[N];    // if applicable, subgroup of species.
  char service[N];  // type of service the animal provides.
  char misc[2*N];   // other special information, specific to each animal.
} animals[MAX],           // for input of new animals.
  animals_all[MAX_CUR];   // current list of animals.

// Main functions
void new_animals();   // add new animal via manual input by user.
void read_inc(int &count);      // add new animal(s) via reading from an external file.
int disp_inc();       // display list of unsaved animals (animals array).
void edit_inc();      // edit incoming animals

void read_cur();           // read in current members from external file.
void updt_cur(int count);      // write unsaved animals to main list
void disp_cur();           // update and display main list of recorded animals.

// Utility functions
void greeting();      // initial greeting and instructions.
void farewell();      // exit message.
void inc_greet();     // instructions for loading external file
int menu();           // recurring menu option for program navigation.

void call_edit(int count);               // prompt to edit incoming animals.
void call_menu(int &selection); // return to menu.
char yes_no(const char* str);   // get a yes/no response.

void reset_incoming();         // clear list of incoming animals
void reset_current();          // reset list to original farm members


//             o  o  O  O  0 0
//            ,______  ____    0
//            | MAIN \_|[]|_'__Y        PROGRAM 3! STRUCTS! EXTERNAL FILES!
//            |_______|__|_|__|} c++                                         79
//=============oo--oo==o--OOO\\================================================
int main() {

  // menu selection variable.
  int selection {0};
  int inc_count {0};

  greeting();

  do {
    selection = menu();
    switch (selection) {
      case 1:
        reset_incoming();
        new_animals();
        inc_count = disp_inc();
        call_edit(inc_count);
        break;
      case 2:
        if (animals[0].name[0] == 0) {
          cout << "\nNo incoming animals, returning to menu..." << endl << endl;
          this_thread::sleep_for(chrono::milliseconds(1500));
        } else {
          inc_count = disp_inc();
          call_edit(inc_count);
        };
        break;
      case 3:
        reset_incoming();
        read_inc(inc_count);
        call_edit(inc_count);
        break;
      case 4:
        disp_cur();
        call_menu(selection);
        break;
      case 5:
        break;
      case 6:
        break;
      case 7:
        reset_current();
        cout << string(69*2, '\n');
        greeting();
        break;
      case 8:
        reset_current();
        farewell();
        break;
    };
  } while (selection < 1 || selection != 8);

  return 0;
};

//=============================================================================
// ┌┬┐┌─┐┬┌┐┌  ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// │││├─┤││││  ├┤ │ │││││   │ ││ ││││└─┐
// ┴ ┴┴ ┴┴┘└┘  └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘


void new_animals() {
  char response {'y'};

  cout << "\nManual addition of new farm members... " << endl << endl;

  for (int i = 0; i < MAX && response == 'y'; i++) {
    cout << "Name: ";
    cin >> animals[i].name;
    cout << "Species: ";
    cin >> animals[i].species;
    cout << "Breed: ";
    cin >> animals[i].breed;
    cout << "Service: ";
    cin >> animals[i].service;
    cout << "Misc: ";
    cin >> animals[i].misc;
    cout << endl;

    if (!(i+1 == MAX)) {
      do {
        (yes_no("Add another?") == 'n') ? response = 'n' : response = 'y';
      } while (!(response == 'y' || response == 'n'));
    } else if (i+1 == MAX) {
      cout << "Max number new animals reached for manual input... Echoing input..." << endl;
      this_thread::sleep_for(chrono::milliseconds(1500));
    };
  };
}


void read_inc(int &inc_count) {
  char new_animals[N];
  int i {0};
  ifstream in_file;

  inc_greet();

  cout << "File name: ";
  cin.get(new_animals, N, '\n');
  cin.ignore(420, '\n');

  in_file.open(new_animals);

  while (in_file && !in_file.eof() && i < MAX) {
    in_file.get(animals[i].name, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals[i].species, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals[i].breed, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals[i].service, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals[i].misc, N, '\n');
    in_file.ignore(100, '\n');

    ++i;

    if (i == MAX && !in_file.eof()) {
      cout << "\n!! Attention !! --- New animal registration can only support "
        << MAX << " animals at once.\nOnly the first "
        << i << " made it in."
        << endl;
      this_thread::sleep_for(chrono::milliseconds(2000));
    };
  };

  in_file.close();
  in_file.clear();

  inc_count = disp_inc();
}

void read_cur() {
  int i {0};
  ifstream in_file;

  in_file.open(CUR_ANIMALS);

  while (in_file && !in_file.eof() && i < MAX_CUR) {
    in_file.get(animals_all[i].name, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals_all[i].species, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals_all[i].breed, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals_all[i].service, N, DLM);
    in_file.ignore(100, DLM);

    in_file.get(animals_all[i].misc, N, '\n');
    in_file.ignore(100, '\n');

    ++i;

    if (i == MAX_CUR && !in_file.eof()) {
      cout << "\n!! Attention !! --- Farm at capacity! Only the first "
        << i << " made it in!"
        << endl;
      this_thread::sleep_for(chrono::milliseconds(2000));
    };
  };

  in_file.close();
  in_file.clear();
}

int disp_inc(){
  int i {0};

  cout << endl << "Displaying incoming farm animals:" << endl << endl;

  while (i < MAX && !(animals[i].name[0] == 0)) {
    cout << "Name: "
      << animals[i].name << "\n";
    cout << "  - Species: "
      << animals[i].species << "\n";
    cout << "  - Breed: "
      << animals[i].breed << "\n";
    cout << "  - Service: "
      << animals[i].service << "\n";
    cout << "  - Misc: "
      << animals[i].misc << "\n" << endl;
    ++i;
  };

  cout << "Total number of new animals: " << i << endl << endl;

  return i;
}

void disp_cur() {
  int i {0};

  memset(animals_all, 0, sizeof(animals_all));
  animals_all[MAX_CUR-1] = animal();

  read_cur();
  cout << endl;

  while (i < MAX_CUR && !(animals_all[i].name[0] == 0)) {
    cout << "Name: "
      << animals_all[i].name << "\n";
    cout << "  - Species: "
      << animals_all[i].species << "\n";
    cout << "  - Breed: "
      << animals_all[i].breed << "\n";
    cout << "  - Service: "
      << animals_all[i].service << "\n";
    cout << "  - Misc: "
      << animals_all[i].misc << "\n"
      << endl;
    ++i;
  };

  cout << "Total number of farm animals: " << i << endl << endl;
}

void updt_cur(int inc_count) {
  cout << endl << "Updating current farm animals..." << endl;

  ofstream out_file;
  out_file.open(CUR_ANIMALS, ios::app);

  if (out_file) {
    for (int i = 0; i < inc_count; i++) {
      out_file
        << animals[i].name << DLM
        << animals[i].species << DLM
        << animals[i].breed << DLM
        << animals[i].service << DLM
        << animals[i].misc << endl;
    };
  out_file.close();
  };

  reset_incoming();
}

void edit_inc() {
  int selection {-1};

  cout << endl;
  for (int i = 0; i < MAX; i++) {
    if (!(animals[i].name[0] == 0)) {
      cout <<"[" << i << "] " << animals[i].name << "\t";
    };

    if (i == 4) cout << endl;
  };
  cout << endl << endl;

  do {
    cout << "Please select one of the above to edit: ";
    cin >> selection;
    cin.clear();
    cin.ignore(420, '\n');
  } while (!(selection > -1 && selection < 9));
}

// How do I split up files properly?
//=============================================================================
// ┬ ┬┌┬┐┬┬ ┌┬┐┬ ┬  ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// │ │ │ ││  │ └┬┘  ├┤ │ │││││   │ ││ ││││└─┐
// └─┘ ┴ ┴┴─┘┴  ┴   └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘


void inc_greet() {
  cout << endl
       << "Automatic animal registration in progress..."
       << endl << endl;
  cout << "Please provide file name of animals you wish to send to the farm.\n"
       << "\t E.g., example_list.txt is provided for demonstration of automatic entries. \n\n"
       << "The Provided file must have lines in format of\n\n"
       << "\tName|Species|Breed|Service|Miscellaneous\n\n"
       << "Please enter \"none\" if these is no extra info associated with the animal,\n"
       << "and \"unsure\" for data for other entries."
       << endl << endl;
}

void menu_greeting() {
  cout
    << endl
    << "\t\t\t\t ╔╦╗┌─┐┌┐┌┬ ┬ \n"
    << "\t\t\t\t ║║║├┤ ││││ │ \n"
    << "\t\t\t\t ╩ ╩└─┘┘└┘└─┘ \n"
    << endl;

  cout
    << "[1] Animal Registration -- Manual\t"
    << "[2] List INCOMING farm members\n"
    << "[3] Animal Registration -- Automatic\t"
    << "[4] List CURRENT farm members \n"
    << "[5] Search current animals by species\t"
    << "[6] Search current animals by breed\n"
    << "[7] Restart\t\t\t\t"
    << "[8] Quit"
    << endl << endl;
}

int menu() {
  int response {0};

  menu_greeting();

  do {
    cout << "Please select a menu option: ";
    cin >> response;
    cin.clear();
    cin.ignore(420, '\n');
  } while (response < 1 || response > 8);

  return response;
}

void reset_incoming() {
  memset(animals, 0, sizeof(animals));
  animals[MAX-1] = animal();
}

void reset_current() {
  if (yes_no("\nReset current animal list?") == 'y') {
    memset(animals_all, 0, sizeof(animals_all));
    animals_all[MAX_CUR-1] = animal();

    ifstream in_file;
    ofstream out_file;

    char line[N*5];

    in_file.open(ORIG_ANIMALS);
    if (in_file) {
      out_file.open(CUR_ANIMALS);
      if (out_file) {
        in_file.get(line, N*6, '\n');
        in_file.ignore(100, '\n');
        while (in_file && !in_file.eof()) {
          out_file << line << endl;
          in_file.get(line, N*6, '\n');
          in_file.ignore(100, '\n');
        }
      };
      out_file.close();
    };
    in_file.close();
  };
}

char yes_no(const char* str) {
  char response;
  do {
    cout << str << " [y/n]: ";
    cin >> response;
    tolower(response);
    cin.ignore(420, '\n');
    if (response == 'n') return 'n';
  } while (response != 'y');

  return 'y';
}

void call_edit(int inc_count) {
  char response;
  do {
    response = yes_no("Would you like to edit any entries?");
    if (response == 'y') edit_inc();
  } while (response != 'n');

  if (yes_no("Update current animals?") == 'y') updt_cur(inc_count);
}

void call_menu (int &selection) {
  do {
    (yes_no("Return to menu? (no = quit)") == 'n') ? selection = 8 : selection = 0;
  } while (selection != 0 && selection != 8);
  if (selection == 8) farewell();
}

void greeting() {
  cout
    << endl
    << "\t\t\t ╔═╗┌┐┌┬┌┬┐┌─┐┬    ╔═╗┌─┐┬─┐┌┬┐ \n"
    << "\t\t\t ╠═╣│││││││├─┤│    ╠╣ ├─┤├┬┘│││ \n"
    << "\t\t\t ╩ ╩┘└┘┴┴ ┴┴ ┴┴─┘  ╚  ┴ ┴┴└─┴ ┴ \n"
    << endl;

  cout
    << "Animals should be equal, free, and happy! All animals described in this program\n"
    << "have not been harmed and provide invaluable services to others that they love."
    << endl << endl;

  cout
    << "This program keep track of animals with that provide such services.\n"
    << "We do our best to make any animal at this farm feel happy and respected."
    << endl << endl;

  cout
    << "Users of this program are free to add new animals manually, or provide\n"
    << "a list of animals that wish to join the farm.\n\n"
    << "\t Max number of new animals: "<< MAX << "\n"
    << "\t Max number of total animals: " << MAX_CUR << "\n\n"
    << "New members of our farm require a name, species, breed, service they \n"
    << "provide to be admitted; other additional information may be added if desired."
    << endl << endl;

  cout
    << "Users may also simply list the animals currently in the farm.\n"
    << "Menu options will be provided to navigate the functionality of this program."
    << endl;
}

void farewell() {
  cout
    << endl
    << "     ╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
    << "     ╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
    << "     ╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
    << endl;
}
