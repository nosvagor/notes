// ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔╦╗┬ ┬┌─┐
// ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││   ║ ││││ │
// ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴   ╩ └┴┘└─┘
// cullyn Newman --- cs 162

// Meta-purpose of this program: exercise and implement arrays/functions.
// The purpose of the program itself is to take a single input supplied by a
// by a user, "decipher" the it, and display a more friendly and readable
// summary of the class.

// styling note: I dislike lining up brackets. I line up the bracket with the
// respective statement the block is associated with, like all other
// programming languages I use do.

#include <iostream>
#include <cstring>
using namespace std;

// Constants
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
  // user input array
  char input[INPUT_SIZE];

  // course name, e.g., cs162
  char course[DESG_SIZE];
  // offering type, e.g., hybrid
  char offering[DESG_SIZE];

  // respective content categories:
  // lect -> lecture
  char lecture[DESG_SIZE];
  // lab -> lab
  char lab[DESG_SIZE];
  // ex -> exam
  char exam[DESG_SIZE];
  // mat -> materials
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
  };

  // exit, or restart.
  farewell();
  return 0;
}

// greeting displays instructions and basic info of the program.
void greeting() {
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

// getClass is simple function to receive user input.
void getClass(char arr[]) {
  cout << "\nPlease enter course information: ";
  cin.get(arr, INPUT_SIZE);
  cin.ignore(420, '\n');
}

// confirm returns a boolean, depending on response; a simple yes/no continue
// function.
bool confirm() {
  char response {};

  do {
    cout << "Is this information correct? [y/n]: ";
    cin >> response;
    cin.ignore(420, '\n');
    if (response == 'n') return false;
  } while (response != 'y');

  return true;
}

// format transforms input into a standardize, all lowercase, form. Ended up
// not being that necessary, but feels like a good approach if program were to
// be extended.
//
// -- Note: further optimization could be applied here to improve later
// functions. I was unsure good practices here and decided against implementing
// it as it served little purpose for the requirements of this program.
void format(char input[]) {
  for (int i = 0; i < strlen(input); ++i){
   input[i] = tolower(input[i]);
   if ((input[i] == ':') || (input[i] == '-') || (input[i] == ',')) {
      input[i] = ' ';
    };
  };
}

// extractCourse gets the course name and offering type based, assuming only
// options to choose from are: "hybrid, online, aa".
void extractCourse(char input[], char course[], char offering[]) {

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
  };

  if (strstr(input, "online")) {
    memcpy(offering, "online", 7);
  };

  if (strstr(input, "aa")) {
    memcpy(offering, "aa", 3);
  };
}

// decipher takes the input arr and updates content arr based on given
// designators. If no designator is supplied, then it defaults to in person.
//
// -- Note: a rather hard-coded approach. I am not happy with this. Fails if
// user inputs spaces between dashes, e.g., lect - r...
void decipher(char input[], char content[], const char *desg) {
  memcpy(content, "in person", 10); // default to in person

  int i = strlen(desg)+1; // get position of designator

  // get result of struts, null results keep default assignment.
  const char *result;
  result = strstr(input, desg);

  // non-null results reassign content category.
  if (result != NULL) {
    char des = strstr(input, desg)[i];
    if (des == 'o') memcpy(content, "optional", 9);
    if (des == 'r') memcpy(content, "remote", 7);
  };
}

// farewell asks user for a restart; re-runs main if yes, else executes
// a basic farewell message.
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
