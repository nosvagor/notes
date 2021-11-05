#include <iostream>
#include <cctype>
#include <cstring>
#include <fstream>

using namespace std;

// constants; N for natural number, standard size
const int N {42};
const int SEC {6};
const int DES {10};

// function declarations
void get_name(struct person & student);
void get_course(struct course & class_one);

// structs
struct person {
  char first[N];
  char middle;
  char last[N];
};

struct course {
  int crn {0};
  char desg[DES];
  char sect[SEC];
};

int main() {

  person student;
  course class_one;

  get_name(student);

  cout << student.first << " "
       << student.middle << " "
       << student.last << endl << endl;

  get_course(class_one);

  cout << class_one.desg << " ("
       << class_one.crn << ") --- "
       << class_one.sect << endl << endl;

  return 0;
};


void get_name(struct person &student){
  cout << "First name: ";
  cin.get(student.first, N, '\n');
  cin.ignore(420, '\n');

  cout << "Middle initial: ";
  cin >> student.middle;
  cin.ignore(420, '\n');

  cout << "Last name: ";
  cin.get(student.last, N, '\n');
  cin.ignore(420, '\n');
}


void get_course(struct course & class_one){
  cout << "Course designator: ";
  cin.get(class_one.desg, N, '\n');
  cin.ignore(420, '\n');

  do {
    cout << "Course CRN: ";
    cin >> class_one.crn;
    cin.clear();
    cin.ignore(420, '\n');
  } while (class_one.crn < 1);

  cout << "Course section: ";
  cin.get(class_one.sect, N, '\n');
  cin.ignore(420, '\n');
}
