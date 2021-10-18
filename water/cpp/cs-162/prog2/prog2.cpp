// ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔╦╗┬ ┬┌─┐
// ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││   ║ ││││ │
// ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴   ╩ └┴┘└─┘
// cullyn newman -- cs 162

// Meta-purpose of this program: exercise and implement arrays/functions.
// The purpose of the program itself is to take a single input supplied by a
// by a user, "decipher" the it, and display a more friendly and readable
// summary of the class.

// User input should come in a semi-normal format, so minimal error checking is
// necessary.


#include <iostream>
#include <cctype>
#include <cstring>
using namespace std;

// Constant
const int INPUT_SIZE {69};
const int DESG_SIZE {30};

// Prototype functions
void greeting();
void getClass(char input[]);
bool confirm();
void format(char input[]);

void farewell();

//             o  o  O  O  0 0
//            ,______  ____    0
//            | MAIN \_|[]|_'__Y
//            |_______|__|_|__|} c++                                         79
//=============oo--oo==oo--OOO\\===============================================
int main() {
  char input[INPUT_SIZE];

  char course[DESG_SIZE];
  char offering[DESG_SIZE];

  char lecture[DESG_SIZE];
  char lab[DESG_SIZE];
  char exam[DESG_SIZE];
  char material[DESG_SIZE];

  greeting();

  do {
    getClass(input);
    cout << "\nYou entered:\n"
         << "\n\t" << input
         << endl << endl;
  } while (!confirm());

  farewell();

  return 0;
}

void greeting(){
  cout << endl
       << "\t\t╔═╗┬  ┌─┐┌─┐┌─┐  ╦┌┐┌┌─┐┌─┐\n"
       << "\t\t║  │  ├─┤└─┐└─┐  ║│││├┤ │ │\n"
       << "\t\t╚═╝┴─┘┴ ┴└─┘└─┘  ╩┘└┘└  └─┘\n"
       << endl;

  cout << "Hello! All we need from you is your course information.\n"
       << "It should look something like this:\n"
       << "\n\t \"CS162 Hybrid: Lab - R, Ex - R, Mat - R\"\n\n"
       << "Don't worry if you don't have all the information; classes are\n"
       << "in person unless otherwise specified. We'll also give you specific\n"
       << "details along the way, if they come up!\n"
       << endl;
}

void getClass(char arr[]){
  cout << "\nPlease enter course information: ";
  cin.get(arr, INPUT_SIZE);
  cin.ignore(420, '\n');
}

bool confirm() {
  char response {};

  do {
    cout << "Is this information correct? [y/n]: ";
    cin >> response;
    cin.ignore(420, '\n');
    if (response == 'n') return 0;
  } while (response != 'y');

  return 1;
}

void format(char input[]) {
  for (int i = 0; i < strlen(input); ++i){
   input[i] = tolower(input[i]);
   if (input[i] == ':' || input[i] == '-' || input[i] == ',') input[i] = ' ';
  }
}

void farewell() {
  cout << endl
       << "╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
       << "╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
       << "╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
       << endl;
}
