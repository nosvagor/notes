// ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔╦╗┬ ┬┌─┐
// ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││   ║ ││││ │
// ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴   ╩ └┴┘└─┘
// cullyn newman -- cs 162

// Meta-purpose of this program: exercise and implement arrays/functions.
// The purpose of the program itself is to take a single input supplied by a
// by a user, "decipher" the it, and display a more friendly and readable
// summary of the class.

#include <iostream>
#include <cctype>
#include <cstring>
using namespace std;

// Constant
const int INPUT_SIZE {69};
const int DESG_SIZE {10};

// Prototype functions
void greeting();
void getClass(char input[]);
bool confirm();
void format(char input[]);
void extractCourse(char input[], char course[], char offering[]);
void decipher(char input[], char content[], const char *desg);
void farewell();

//             o  o  O  O  0 0
//            ,______  ____    0
//            | MAIN \_|[]|_'__Y                PROGRAM 2! ARRAYS!
//            |_______|__|_|__|} c++                                         79
//=============oo--oo==oo--OOO\\===============================================
int main() {
  char input[INPUT_SIZE];

  // basic input
  char course[DESG_SIZE];
  char offering[DESG_SIZE];

  // hybrid designators, defaults to in person
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

  format(input);
  extractCourse(input, course, offering);

  if (!strcmp("online", offering)) {
    cout << endl << course
      << " is offered as an online class! "
      << "All content will be be available remotely."
      << endl << endl;
  };

  if (!strcmp("aa", offering)) {
    cout << endl << course
      << " is offered as an attend-anywhere class! "
      << "All content is available online,\n"
      << "but any labs, lectures, or exams are offered in person if preferred."
      << endl << endl;
  };

  if (!strcmp("hybrid", offering)) {

    decipher(input, lecture, "lect");
    decipher(input, lab, "lab");
    decipher(input, exam, "ex");
    decipher(input, material, "mat");
  }

  cout << lecture << endl;
  cout << lab << endl;
  cout << exam << endl;
  cout << material << endl;


  char response {};
  do {
    cout << "Would you like to restart? [y/n]: ";
    cin >> response;
    cin.ignore(420, '\n');
  } while (!((response == 'n') || (response == 'y')));

  if (response == 'y') {
    main();
  } else farewell();

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
       << "\n\t \"CS162 AA\"\n"
       << "\t \"CS162 Online\"\n"
       << "\t \"CS162 Hybrid: Lect-O, Lab-R, Ex-R, Mat-R\"\n"

       << "\nOnline: all classes and content are online.\n"
       << "AA: all classes and content are up to you, remote and in person is available.\n"
       << "Hybrid: a combination of in person and remote options;\n"
       << "  -O indicates \"Optional\", i.e., specifics are provided both remotely and in person.\n"
       << "  -R indicates \"Remote\", i.e., this portion of the class is remote only.\n"

       << "\nClasses are assumed to be in person unless otherwise specified."
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
   if ((input[i] == ':') || (input[i] == '-') || (input[i] == ',')) {
      input[i] = ' ';
    }
  }
}

void extractCourse(char input[], char course[], char offering[]){

  int size {0};
  for (int i = 0; input[i] != ' '; ++i){
    course[i] = toupper(input[i]);
    size += 1;
  }
  course[size] = '\0';


  if (strstr(input, "hybrid")) {
    memcpy(offering, "hybrid", 7);
  }

  if (strstr(input, "online")) {
    memcpy(offering, "online", 7);
  }

  if (strstr(input, "aa")) {
    memcpy(offering, "aa", 7);
  }
}

void decipher(char input[], char content[], const char *desg){
  memcpy(content, "in person", 10);

  int i = strlen(desg)+1;

  const char *result;
  result = strstr(input, desg);

  if (result != NULL) {
    char des = strstr(input, desg)[i];
    if (des == 'o') memcpy(content, "optional", 9);
    if (des == 'r') memcpy(content, "remote", 7);
  }
}

void farewell() {
  cout << endl
       << "╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
       << "╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
       << "╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
       << endl;
}
