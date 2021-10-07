/* ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔═╗┌┐┌┌─┐ */
/* ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││  ║ ║│││├┤  */
/* ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴  ╚═╝┘└┘└─┘ */
/* Cullyn Newman --- CS 162 */
/* Purpose: calculate the price of a rental stay, accounting for potential
 * discounts or fees.  */

#include <iostream>
#include <string>
using namespace std;

// global functions and variables used in program
// tasks broken down to functions
// I doubt using global variables like this is a good way to go about things.
void greeting();
void getData();
  int rate = 0;
  int tripLength = 0;
  int daysUntilTrip = 0;
void errorCheck();
void calculate();
  int initialCost = 0;
void calculateDiscounts();
  int tripCost = 0;
  int discounts = 0;
  int savings = 0;
  int serviceCost = 0;
  int totalCost = 0;
void results();


//             o  o  O  O  0 0
//            ,______  ____    0
//            | main \_|[]|_'__Y
//            |_______|__|_|__|}
//=============oo--oo==oo--OOO\\====================
int main() {
  greeting();
  getData();
  errorCheck();
  calculate();
  results();
  return 0;
}

void greeting(){
  cout << "\nWelcome to the... \n\n"
          "\t╔╦╗┬ ┬┌─┐  ╔═╗┌─┐┌┬┐┬ ┬┌─┐┬    ╔═╗┬─┐┬┌─┐┌─┐┬\n"
          "\t ║ ├─┤├┤   ╠═╣│   │ │ │├─┤│    ╠═╝├┬┘││  ├┤ │\n"
          "\t ╩ ┴ ┴└─┘  ╩ ╩└─┘ ┴ └─┘┴ ┴┴─┘  ╩  ┴└─┴└─┘└─┘o"
  << endl << endl;

  cout << "All we need from you is: \n"
          "\t - the nightly rate, \n"
          "\t - duration of your trip, \n"
          "\t - and how many days until the start of your vacation! \n"
          "We will calculate the actual price, accounting for any "
          "fees and discounts."
  << endl << endl;

  cout << "Assumed fees and discounts:\n"
          "\t - 10\% discount for stays longer than 3 days \n"
          "\t - 20\% discount for booking more than 5 days in advance \n"
          "\t - $50 cleaning fee for says longer than 3 days \n"
          "\t - 1\% service fee (applied prior to discounts)"
  << endl << endl;
}

void getData(){

  // lambda functions, couldn't get recursion working.
  // probably the wrong way of doing this
  auto getRate = [&](){
    cout << "Nightly rate (USD): ";
    cin >> ::rate;
  };

  auto getTripLength = [&](){
    cout << "Length of trip (days): ";
    cin >> ::tripLength;
  };

  auto getDaysUntilTrip = [&](){
    cout << "Time until trip (days): ";
    cin >> ::daysUntilTrip;
  };

  // unsafe error but simple checking, assuming only integers will be entered
  getRate();
  while (::rate <= 0){
    cout << "Rate invalid, please enter price that is greater than 0." << endl;
    getRate();
  }

  getTripLength();
  while (::tripLength <= 0){
    cout << "Trip length invalid, please enter a duration that is at least 1 day." << endl;
    getTripLength();
  }

  getDaysUntilTrip();
  while (::daysUntilTrip < 0){
    cout << "Start date invalid, we do not provide a time travel service." << endl;
    getDaysUntilTrip();
  }

  // echo data to user
  cout << "\nNightly rate is $" << ::rate << endl;
  cout << "The duration of your trip is " << ::tripLength << " day(s)" << endl;
  cout << "Your trip starts in " << ::daysUntilTrip << " day(s)" << endl;
};

void errorCheck(){
  char response;

  // allow user to make sure data is correct
  do {
  cout << "\nIs the above information correct? [y/n]: ";
  cin >> response;
  } while (response != 'y' && response != 'n');

  // how do I use strings? I'd prefer to use 'yes' and 'no' as well.
  // additionally, this takes inputs if more is typed than 'y' and 'n'
  // how do I fix this?
  // also, how do I make the default selection 'y' if just enter is pressed?
  if (response == 'n') {
    getData();
    errorCheck();
  }
};

void calculate(){

  // calculate initial costs before discounts and fees
  ::initialCost = ::rate * ::tripLength;

  // 20% discount for early booking
  if (::daysUntilTrip > 5) ::discounts += 20;

  // 10% discount and $50 cleaning fee for trips > 3 days.
  if (::tripLength > 3) {
    ::discounts += 10;
    ::serviceCost += 50;
  };

  // apply discounts and fees
  ::savings += ::initialCost * ::discounts / 100;
  ::tripCost += ::initialCost - ::savings;
  ::serviceCost += ::tripCost * 0.01;
  ::totalCost += ::tripCost + ::serviceCost;


};

void results(){
  char response;

  cout << "\nThe ACTUAL costs of your trip:" << endl;

  cout << "\t- Initial cost:\t\t\t$"
    << ::initialCost
  << endl;

  cout << "\t- Savings ("
    << ::discounts << "%): \t\t-$"
    << ::savings
  << endl;

  cout << "\t- Trip cost:\t\t\t$"
    << ::tripCost
  << endl;

  cout << "\t- Service cost:\t\t\t$"
    << ::serviceCost
  << endl;

  cout << "\t- Total cost:\t\t\t$"
    << ::totalCost
  << endl << endl;

  do {
  cout << "Would you like to restart? [y/n]: ";
  cin >> response;
  } while (response != 'y' && response != 'n');

  if (response == 'y') main();
  else { cout <<
    "\n ██████╗ ██╗  ██╗       ██████╗ ██╗   ██╗███████╗██╗       ██╗\n"
      "██╔═══██╗██║ ██╔╝       ██╔══██╗╚██╗ ██╔╝██╔════╝██║    ██╗╚██╗\n"
      "██║   ██║█████╔╝        ██████╔╝ ╚████╔╝ █████╗  ██║    ╚═╝ ██║\n"
      "██║   ██║██╔═██╗        ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝    ██╗ ██║\n"
      "╚██████╔╝██║  ██╗▄█╗    ██████╔╝   ██║   ███████╗██╗    ╚═╝██╔╝\n"
      " ╚═════╝ ╚═╝  ╚═╝╚═╝    ╚═════╝    ╚═╝   ╚══════╝╚═╝       ╚═╝"
   << endl;
  };
};











