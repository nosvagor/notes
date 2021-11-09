// ┌─┐┬  ┌─┐┌─┐┌─┐┌─┐┌─┐
// │  │  ├─┤└─┐└─┐├┤ └─┐
// └─┘┴─┘┴ ┴└─┘└─┘└─┘└─┘
// cullyn --- cs162
// Purpose: this file implements class methods. Includes animal class (for each
// specific animal), and animals class (used to manage a collection of
// animals).

#include "main.h"

//=============================================================================

// ┌─┐┌┐┌┬┌┬┐┌─┐┬
// ├─┤│││││││├─┤│
// ┴ ┴┘└┘┴┴ ┴┴ ┴┴─┘
// Object used to keep track of information about each animal.

// constructor, class only has char arrays
animal::animal() {
  name = NULL;
  species = NULL;
  breed = NULL;
  service = NULL;
  misc = NULL;
}


// destructor; I wanted to use dynamically sized arrays.
animal::~animal() {
  if (name) {
    delete [] name;
    delete [] species;
    delete [] breed;
    delete [] service;
    delete [] misc;
  }

  // I hope calling the constructor isn't bad practice, it seems to work fine.
  animal();
}


// get_info takes in a string prompt and member object then returns a
// dynamically sized array.
void animal::get_info(const char * str, char *& info) {
  char temp[SIZE];

  do {
    cout << str ;
    cin.get(temp, SIZE, '\n');
    cin.clear();
    cin.ignore(SIZE, '\n');
  } while (!temp[0]);

  info = new char [strlen(temp) + 1];
  strcpy(info, temp);
}


// read_manual applies get_info function, for each member.
void animal::read_manual() {
  cout << endl;
  get_info("Name of animal: ", name);
  get_info("Species: ", species);
  get_info("Breed: ", breed);
  get_info("Service: ", service);
  get_info("Additional information: ", misc);
}


// get_info reads in lines from an external file instead of manually, still
// creating dynamically sized arrays for each member.
void animal::get_info_auto(char *& info, char dlm, ifstream & in_file) {
  char temp[SIZE];

  in_file.get(temp, SIZE, dlm);
  in_file.ignore(SIZE, dlm);

  if (strlen(temp) == 0) return;

  info = new char [strlen(temp) + 1];
  strcpy(info, temp);
}


// read_auto applies the get_info_auto function.
void animal::read_auto(ifstream & in_file) {
  get_info_auto(name, DLM, in_file);
  get_info_auto(species, DLM, in_file);
  get_info_auto(breed, DLM, in_file);
  get_info_auto(service, DLM, in_file);
  get_info_auto(misc, '\n', in_file);
}


// display displays all information confined in the object, and returns false
// if object is empty; boolean is used for error checking when called in case
// there are empty class objects in the initially created list.
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


// update will write each object of the animal class to the external animal
// file (sac/animals.txt).
void animal::update(int animal_count) {
  ofstream out_file;
  out_file.open(CURRENT, ios::app);

  out_file
    << name << DLM
    << species << DLM
    << breed << DLM
    << service<< DLM
    << misc << endl;

  out_file.close();
}


// compare returns true if given char array matches one of member arrays.
bool animal::compare(char * match, const char * info) {

  if (!name) return false; // noting in array, return.

  // probably a better way to pass in desired member to compare, but I'm not
  // sure how. Currently hard coded, if I were to extend search to any member
  // field, then I would find a better way.

  if (!strcmp("species", info)) {
    if (!strcmp(match, species)) {
      display();
      return true;
    }
  }

  if (!strcmp("breed", info)) {
    if (!strcmp(match, breed)) {
      display();
      return true;
    }
  }

  return false;
}


// ┌─┐┌┐┌┬┌┬┐┌─┐┬  ┌─┐
// ├─┤│││││││├─┤│  └─┐
// ┴ ┴┘└┘┴┴ ┴┴ ┴┴─┘└─┘
// Object used to differentiate between groups of animals (incoming vs current)


// constructor
animals::animals() {

  group = new animal[MAX];
  animal_count = 0;

}

// destructor
animals::~animals() {

  // group indicates list of animals, i.e., incoming or current (used in this
  // program).
  if (!group) delete [] group;
  group = NULL;
  animal_count = 0;

}


// read_all calls the read_manual function on the animal class and updates the
// array of objects contained in the animal class.
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


// read_all_auto calls the read_auto function on each object in the array of
// objects (group) using supplied external file.
void animals::read_all_auto() {

  // new_count keeps track of new animals added in order to no exceed farm
  // capacity.
  int new_count {0};

  // new_animals is the file name, if the user chooses to provide their own.
  char new_animals[SIZE];
  ifstream in_file;

  // basic instructions for user.
  incoming_greeting();

  // use example file (src/example_list.txt) or custom file path.
  if (yes_no("Use example file?") == 'y') {
    in_file.open(EXAMPLE);
  } else {
    cout << "File name: ";
    cin.get(new_animals, SIZE, '\n');
    cin.ignore(SIZE, '\n');
    in_file.open(new_animals);
  }

  // make sure custom file is valid, if supplied.
  if (!in_file) {
    cout << "\n  !! Warning --- Unable to read file." << endl;
    return_to_menu();
  }

  // execute read_auto function, reading in new objects.
  while (animal_count < MAX && in_file && !in_file.eof()) {
     group[animal_count].read_auto(in_file);
     ++animal_count;
     ++new_count;
  }

  // warning if file contains more objects than max capacity allows.
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


// read_file_only is used to read and update current animals list, since
// current list is saved to an re-read each time using an external file in
// order to save state between program sessions.
void animals::read_file_only() {

  ifstream in_file;

  in_file.open(CURRENT);

  while (animal_count < MAX && in_file && !in_file.eof()) {
     group[animal_count].read_auto(in_file);
     ++animal_count;
  }

  // warning if file contains more objects than max capacity allows.
  if (in_file && animal_count >= MAX) {
    cout << "\n  !! Warning --- Farm at max capacity ("
         << MAX << "), only the first "
         << animal_count << " made it in."
         << endl;
  }

  in_file.close();
  in_file.clear();
}



// display_all simply calls the display function on each object in the group.
void animals::display_all() {
  bool empty = true;

  for (int i = 0; i < animal_count; ++i) {
    empty = group[i].display();
  }
}


// call_update is a prompt to check if user would like to update current
// animals with incoming animals list.
bool animals::call_update() {
  if (yes_no("\nUpdate current animals?") == 'y') {

    for (int i = 0; i < animal_count; ++i) {
      group[i].update(animal_count);
    }

    return true;
  }

  return false;
}


// search is used find particular breed or species by calling compare function
// in animal class. Further search requirements were not implemented, only the
// required in this case.
void animals::call_compare(const char * info) {

  int count = 0;

  char match[SIZE];

  cout << "\nSearch (" << info << "): ";
  cin.get(match, SIZE, '\n');
  cin.ignore(SIZE, '\n');

  cout << "\n\n\t\t\t ======== SEARCH RESULTS ========" << endl;

  for (int i = 0; i < animal_count; ++i) {
    if (group[i].compare(match, info)) ++count;
  }

  cout << "\nTotal number of matches: " << count << endl;
}

