// ┌─┐┬  ┌─┐┌─┐┌─┐┌─┐┌─┐
// │  │  ├─┤└─┐└─┐├┤ └─┐
// └─┘┴─┘┴ ┴└─┘└─┘└─┘└─┘
// cullyn --- cs162
// Purpose: this file implementations class methods

#include "main.h"

//=============================================================================

// ┌─┐┌┐┌┬┌┬┐┌─┐┬
// ├─┤│││││││├─┤│
// ┴ ┴┘└┘┴┴ ┴┴ ┴┴─┘
// Object used to keep track of information about each animal.


animal::animal() {
  name = NULL;
  species = NULL;
  breed = NULL;
  service = NULL;
  misc = NULL;
}

animal::~animal() {
  if (name) {
    delete [] name;
    delete [] species;
    delete [] breed;
    delete [] service;
    delete [] misc;
  }

  animal();
}


void animal::get_info(const char * str, char *& info) {
  char temp[SIZE];

  cout << str ;
  cin.get(temp, SIZE, '\n');
  cin.ignore(SIZE, '\n');

  info = new char [strlen(temp) + 1];
  strcpy(info, temp);
}

void animal::read_manual() {
  get_info("name: ", name);
  get_info("species: ", species);
  get_info("breed: ", breed);
  get_info("service: ", service);
  get_info("misc: ", misc);
}

void animal::get_info_auto(char *& info, char dlm, ifstream & in_file) {
  char temp[SIZE];

  in_file.get(temp, SIZE, dlm);
  in_file.ignore(SIZE, dlm);

  if (strlen(temp) == 0) return;

  info = new char [strlen(temp) + 1];
  strcpy(info, temp);
}

void animal::read_auto(ifstream & in_file) {
  get_info_auto(name, DLM, in_file);
  get_info_auto(species, DLM, in_file);
  get_info_auto(breed, DLM, in_file);
  get_info_auto(service, DLM, in_file);
  get_info_auto(misc, '\n', in_file);
}



bool animal::display() {

  if (!name) {
    return false;
  }

  cout << "\nName: " << name
       << "\n  - Species: " << species
       << "\n  - Breed: " << breed
       << "\n  - Service: " << service
       << "\n  - Misc: " << misc
       << endl;

  return true;
}



void animal::edit() {}


bool animal::compare() {

  return false;
}



// ┌─┐┌┐┌┬┌┬┐┌─┐┬  ┌─┐
// ├─┤│││││││├─┤│  └─┐
// ┴ ┴┘└┘┴┴ ┴┴ ┴┴─┘└─┘
// Object used to differentiate between groups of animals (incoming vs current)


animals::animals() {

  group = new animal[MAX];
  animal_count = 0;

}

animals::~animals() {

  if (!group) delete [] group;
  group = NULL;
  animal_count = 0;

}


void animals::read_all() {

  char response = 'y';

  while (response != 'n' && animal_count < MAX) {
     group[animal_count].read_manual();
     ++animal_count;
     response = yes_no("\nAdd another?");
  }

  if (response && animal_count >= MAX) {
    cout << "\n!! Warning !! Farm at max capacity, cannot add another animal :("
         << endl;
    return_to_menu();
  }
}


void animals::read_all_auto() {

  int new_count {0};
  char new_animals[SIZE];
  ifstream in_file;

  incoming_greeting();

  if (yes_no("Use example file?") == 'y') {
    in_file.open(EXAMPLE);
  } else {
    cout << "File name: ";
    cin.get(new_animals, SIZE, '\n');
    cin.ignore(SIZE, '\n');
    in_file.open(new_animals);
  }

  if (!in_file) {
    cout << "\n  !! Warning --- Unable to read file." << endl;
    return_to_menu();
  }

  while (animal_count < MAX && in_file && !in_file.eof()) {
     group[animal_count].read_auto(in_file);
     ++animal_count;
     ++new_count;
  }

  if (in_file && animal_count >= MAX) {
    cout << "\n  !! Warning --- Farm at max capacity ("
         << MAX << "), "
         << new_count << " new animals were registered."
         << endl;
    return_to_menu();
  }

  in_file.close();
  in_file.clear();
}


void animals::read_file_only() {

  ifstream in_file;

  in_file.open(CURRENT);

  while (animal_count < MAX && in_file && !in_file.eof()) {
     group[animal_count].read_auto(in_file);
     ++animal_count;
  }

  if (in_file && animal_count >= MAX) {
    cout << "\n  !! Warning --- Farm at max capacity ("
         << MAX << "), only the first "
         << animal_count << " made it in."
         << endl;
  }

  in_file.close();
  in_file.clear();
}



void animals::display_all() {
  cout << "\nDisplaying incoming farm animals:" << endl;

  bool empty = true;

  for (int i = 0; i < MAX; ++i) {

    if (i == 0 && !empty) {
      cout << "\n incoming animals" << endl;
      return_to_menu();
      return;
    }

    empty = group[i].display();
  }
}



void animals::call_edit() {}



bool animals::search() {

  return false;
}

