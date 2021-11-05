// ╔═╗┬─┐┌─┐┌─┐┌┬┐┬┌┐┌┌─┐┌─┐
// ║ ╦├┬┘├┤ ├┤  │ │││││ ┬└─┐
// ╚═╝┴└─└─┘└─┘ ┴ ┴┘└┘└─┘└─┘
// cullyn --- cs162
// Purpose: functions that are essentially just cout statements.

#include "main.h"


// greeting displays basics instructions on program start and restart
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
    << "\t Max number of new animals: " << INC << "\n"
    << "\t Max number of total animals: " << CUR << "\n\n"
    << "New members of our farm require a name, species, breed, service they \n"
    << "provide to be admitted; other additional information may be added if desired."
    << endl << endl;

  cout
    << "Users may also simply list the animals currently in the farm.\n"
    << "Menu options will be provided to navigate the functionality of this program."
    << endl;
}


// incoming_greeting displays instructions for loading an external file for
// animal registration.
void incoming_greeting() {
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


// menu_greeting simply displays menu options; is used in menu function.
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


// farewell displays a fun farewell message.
void farewell() {
  cout
    << endl
    << "     ╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
    << "     ╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
    << "     ╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
    << endl;
}
