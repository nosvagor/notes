// ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔═╗┌┐┌┌─┐
// ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││  ║ ║│││├┤
// ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴  ╚═╝┘└┘└─┘
// cullyn newman --- cs 162
// purpose: calculate the price of a rental stay, accounting for potential
// discounts or fees.

#include <iostream>
#include <cmath>
#include <string>
using namespace std;

void greeting();
int getRate(int &rate);
int getLength(int &tripLength);
int getDays(int &daysUntilTrip);
void errorCheck();
void calculate();
void results();


//             o  o  O  O  0 0
//            ,______  ____    0
//            | MAIN \_|[]|_'__Y
//            |_______|__|_|__|} c++
//=============oo--oo==oo--OOO\\===============================================
int main() {
  int rate, tripLength, daysUntilTrip, initialCost = {0};
  int tripCost, discounts, savings, serviceCost, totalCost = {0};

  greeting();

  rate = getRate(rate);
  tripLength = getLength(tripLength);
  daysUntilTrip = getDays(daysUntilTrip);

  errorCheck();
  calculate();
  results();
  return 0;
}

void greeting(){
  cout << "\nWelcome to the... \n\n"
          "\t\t╔╦╗┬ ┬┌─┐  ╔═╗┌─┐┌┬┐┬ ┬┌─┐┬    ╔═╗┬─┐┬┌─┐┌─┐┬\n"
          "\t\t ║ ├─┤├┤   ╠═╣│   │ │ │├─┤│    ╠═╝├┬┘││  ├┤ │\n"
          "\t\t ╩ ┴ ┴└─┘  ╩ ╩└─┘ ┴ └─┘┴ ┴┴─┘  ╩  ┴└─┴└─┘└─┘o"
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
          "\t - 1\% service fee (applied AFTER to discounts)"
  << endl << endl;
}

int getRate(int &rate){

  do {
    cout << "Nightly rate (USD): ";
    cin >> rate;
    cin.ignore(100, '\n');
    if (rate <= 0) {
      cout << "You're telling me they are paying YOU to stay here?\n"
           << "What do you need us for then?\n"
           << "Please enter an amount greater than 0."
      << endl;
    };
  } while (rate <= 0);

  return rate;
}

int getLength(int &tripLength){
  // get trip duration, same error check
  do {
    cout << "Trip duration (days): ";
    cin >> tripLength;
    cin.ignore(100, '\n');
    if (tripLength <= 0) {
      cout << "Slow down speedracer, a trip has to be least 1 day long." << endl;
      cout << "Please enter a trip duration longer than 1 day: " << endl;
    };
  } while (tripLength < 1);

  return tripLength;
}

int getDays(int &daysUntilTrip){
  // get days until start fo trip, same error check
  do {
    cout << "Days until your trip: ";
    cin >> daysUntilTrip;
    cin.ignore(100, '\n');
    if (daysUntilTrip <= 0) {
      cout << "Please enter how many days until the start of your trip:  " << endl;
      cout << "start date invalid, we do not provide a time travel service." << endl;
    };
  } while (daysUntilTrip < 0);

  return daysUntilTrip;
};

void errorCheck(&rate, &tripLength, &daysUntilTrip){
  string response;

  // echo data to user
  cout << "\nYour nightly rate is $" << rate << endl;
  cout << "The duration of your trip is " << tripLength << " day(s)" << endl;
  cout << "Your trip starts in " << daysUntilTrip << " day(s)" << endl;

  do {
    cout << "\nIs the above information correct? [yes/no]: ";
    cin >> response;
    cin.ignore(100, '\n');
  } while (response != "y" &&
           response != "yes" &&
           response != "n" &&
           response != "no");

  // how do I use strings? I'd prefer to use 'yes' and 'no' as well.
  // additionally, this takes inputs if more is typed than 'y' and 'n'
  // how do I fix this?
  // also, how do I make the default selection 'y' if just enter is pressed?
  if (response == "n" || response == "no") {
    getData();
    errorCheck();
  };
};

void calculate(){

  // calculate initial costs before discounts and fees
  initialCost = rate * tripLength;

  // 20% discount for early booking
  if (daysUntilTrip > 5) discounts += 20;

  // 10% discount and $50 cleaning fee for trips > 3 days.
  if (tripLength > 3) {
    discounts += 10;
    serviceCost += 50;
  };

  // apply discounts and fees
  savings += round(initialCost * discounts / 100);
  tripCost += initialCost - savings;
  serviceCost += round(tripCost * 0.01);
  totalCost += tripCost + serviceCost;

};

void results(){
  string response;

  cout << "\nThe ACTUAL costs of your trip:" << endl;

  cout << "\t- Initial cost:\t\t\t$"
    << initialCost
  << endl;

  cout << "\t- Savings ("
    << discounts << "%): \t\t-$"
    << savings
  << endl;

  cout << "\t- Trip cost:\t\t\t$"
    << tripCost
  << endl;

  cout << "\t- Service cost:\t\t\t$"
    << serviceCost
  << endl;

  cout << "\t- Total cost:\t\t\t$"
    << totalCost
  << endl << endl;

  do {
    cout << "Would you like to restart? [yes/no]: ";
    cin >> response;
    cin.ignore(100, '\n');
  } while (response != "y" &&
           response != "yes" &&
           response != "n" &&
           response != "no");

  if (response == "y" || response == "yes") {
    rate = tripLength = daysUntilTrip = initialCost = 0;
    tripCost = discounts = savings = serviceCost = totalCost = 0;
    main();
  } else { cout << "\n"
    "╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
    "╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
    "╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
   << endl;
  };
};
