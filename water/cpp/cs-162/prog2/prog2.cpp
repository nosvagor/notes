// ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔╦╗┬ ┬┌─┐
// ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││   ║ ││││ │
// ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴   ╩ └┴┘└─┘
// cullyn newman --- cs 162

// Meta-purpose of this program: exercise and implement arrays/functions.
// The purpose of the program itself is to take a single input supplied by a
// by a user, "decipher" the it, and display a more friendly and readable
// summary of the class.

#include <iostream>
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
  // input array
  char input[INPUT_SIZE];

  // basic information
  char course[DESG_SIZE];
  char offering[DESG_SIZE];

  // hybrid designators
  char lecture[DESG_SIZE];
  char lab[DESG_SIZE];
  char exam[DESG_SIZE];
  char material[DESG_SIZE];

  greeting();

  // get, echo, and confirm user entered information.
  do {
    getClass(input);
    cout << "\nYou entered:\n"
         << "\n\t" << input
         << endl << endl;
  } while (!confirm());

  // make string easier to work with
  format(input);

  // extract course name and offering type
  extractCourse(input, course, offering);

  // results, if course is online
  if (!strcmp("online", offering)) {
    cout << endl << course
      << " is offered as an "<< offering << " class! "
      << "All content will be be available remotely."
      << endl << endl;
  };

  // results, if course is attend anywhere
  if (!strcmp("aa", offering)) {
    cout << endl << course
      << " is offered as an "<< offering << " class! "
      << "All content is available online,\n"
      << "but any labs, lectures, or exams are offered in person if preferred."
      << endl << endl;
  };

  // extract course content if hybrid, defaults to in person if not specified.
  if (!strcmp("hybrid", offering)) {
    decipher(input, lecture, "lect");
    decipher(input, lab, "lab");
    decipher(input, exam, "ex");
    decipher(input, material, "mat");

    // results, if course is hybrid
    cout << endl << course
      << " is offered as an "<< offering << "class!\n"
      << "   - Lectures are " << lecture << ";\n"
      << "   - labs are " << lab << ";\n"
      << "   - exams are " << exam << ";\n"
      << "   - and course materials are " << material << "."
      << endl << endl;
  }

  // exit, or restart.
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

// used to confirm if entered information is correct
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

// turn input to lower case, remove any unusual characters(:-,)
// that might mess up extraction.
void format(char input[]) {
  for (int i = 0; i < strlen(input); ++i){
   input[i] = tolower(input[i]);
   if ((input[i] == ':') || (input[i] == '-') || (input[i] == ',')) {
      input[i] = ' ';
    }
  }
}

// extract course and offering type.
void extractCourse(char input[], char course[], char offering[]){

  // extract course, keep track of size in order to add terminating character
  // for array. Was an issue when restarting program.
  int size {0};
  for (int i = 0; input[i] != ' '; ++i){
    course[i] = toupper(input[i]);
    size += 1;
  }
  course[size] = '\0';


  // overwrite contents of offering with memcpy, if relevant substr is found.
  // more curse offerings can easily be added.
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

// get designator, semi-hard coded assuming format like lect-o, lect-r.
// not sure of a better way, without regex.
// Fragile function, should be fixed.
void decipher(char input[], char content[], const char *desg){
  memcpy(content, "in person", 10); // default to in person

  int i = strlen(desg)+1; // get position of designator

  // get result of strstr, null results keep default assignment.
  const char *result;
  result = strstr(input, desg);

  // non-null results reassign content category.
  if (result != NULL) {
    char des = strstr(input, desg)[i];
    if (des == 'o') memcpy(content, "optional", 9);
    if (des == 'r') memcpy(content, "remote", 7);
  }
}

void farewell() {

  // ask to restart of exit
  char response {};
  do {
    cout << "Would you like to restart? [y/n]: ";
    cin >> response;
    cin.ignore(420, '\n');
  } while (!((response == 'n') || (response == 'y')));

  if (response == 'y') {
    main();
  } else
  cout << endl
       << "╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
       << "╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
       << "╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
       << endl;
}
