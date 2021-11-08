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

// class animal {
//   public:
//     animal();
//     ~animal();

//     void get_info(const char * str, char *& info);
//     void read();
//     void display();
//     void edit();
//     bool compare();

//   private:
//     char * name;
//     char * species;
//     char * breed;
//     char * service;
//     char * misc;
// };

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
  char temp[69];

  cout << str ;
  cin.get(temp, 69, '\n');
  cin.ignore(69, '\n');

  info = new char [strlen(temp) + 1];
  strcpy(info, temp);
}

void animal::read() {
  get_info("name: ", name);
  get_info("species: ", species);
  get_info("breed: ", breed);
  get_info("service: ", service);
  get_info("misc: ", misc);
}



void animal::display() {
  if (!name) {
    cout << "IS NULL" << endl;
    return;
  }

  cout
    << name << '\t' << species << '\t' << breed << '\t' << service << '\t'
    << misc << endl;
}



void animal::edit() {}


bool animal::compare() {

  return false;
}



// ┌─┐┌┐┌┬┌┬┐┌─┐┬  ┌─┐
// ├─┤│││││││├─┤│  └─┐
// ┴ ┴┘└┘┴┴ ┴┴ ┴┴─┘└─┘
// Object used to differentiate between groups of animals (incoming vs current)

// class animals {
//   public:
//     animals();
//     ~animals();

//     void read_all();
//     void display_all();
//     void call_edit();
//     bool search();

//   private:
//     animal group[MAX];
//     int animal_count;
// };

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

  while (response == 'y' && animal_count < MAX) {
     group[animal_count].read();
     ++animal_count;
     response = yes_no("Add another?");
  }

  if (response && animal_count >= MAX) {
    cout << "!! Warning !! Farm at max capacity, cannot add another animal :(" << endl;
    sleep(1500);
  }
}



void animals::display_all() {
  for (int i = 0; i < MAX; ++i) group[i].display();
}



void animals::call_edit() {}



bool animals::search() {

  return false;
}

