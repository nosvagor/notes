// ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔═╗┌┐┌┌─┐
// ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││  ║ ║│││├┤
// ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴  ╚═╝┘└┘└─┘
// cullyn newman --- cs 162
// purpose: calculate the price of a rental stay, accounting for potential
// discounts or fees.

#include <iostream>
#include <cmath> // used for rounding
#include <string> // used for response, not sure how to use arrays yet
using namespace std;

void greeting();


//             o  o  O  O  0 0
//            ,______  ____    0
//            | MAIN \_|[]|_'__Y
//            |_______|__|_|__|} c++
//=============oo--oo==oo--OOO\\===============================================
int main() {

  // variables; I'd prefer to use a map or a class, but I'm not sure how to use
  // them yet.
  int rate = 0;
  int tripLength = 0;
  int daysUntilTrip = 0;
  int initialCost  = 0;
  int tripCost = 0;
  int discounts = 0;
  int savings = 0;
  int serviceCost = 0;
  int totalCost = 0;
  string responseContinue;
  string responseRestart;

  greeting();

  // tried to make functions to get data, wasn't sure how to pass variables
  // outside of scope. Wrapped it inside of a do while loop instead.
  do {
    // get nightly rate
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

    // get length of trip
    do {
      cout << "Trip duration (days): ";
      cin >> tripLength;
      cin.ignore(100, '\n');
      if (tripLength <= 0) {
        cout << "Slow down speedracer, a trip has to be least 1 day long." << endl;
        cout << "Please enter a trip duration longer than 1 day: " << endl;
      };
    } while (tripLength < 1);

    // get days until trip
    do {
      cout << "Days until your trip: ";
      cin >> daysUntilTrip;
      cin.ignore(100, '\n');
      if (daysUntilTrip <= 0) {
        cout << "Please enter how many days until the start of your trip:  " << endl;
        cout << "start date invalid, we do not provide a time travel service." << endl;
      };
    } while (daysUntilTrip < 0);

    // echo data to user
    cout << "\nYour nightly rate is $" << rate << endl;
    cout << "The duration of your trip is " << tripLength << " day(s)" << endl;
    cout << "Your trip starts in " << daysUntilTrip << " day(s)" << endl;

    // ask for corrections
    do {
      cout << "\nIs the above information correct? [yes/no]: ";
      cin >> responseContinue;
      cin.ignore(100, '\n');
    } while (responseContinue != "y" &&
        responseContinue != "yes" &&
        responseContinue != "n" &&
        responseContinue != "no");

  } while (responseContinue == "n" || responseContinue == "no");

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

  // echo results
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

  // ask to restart
  do {
    cout << "Would you like to restart? [yes/no]: ";
    cin >> responseRestart;
    cin.ignore(100, '\n');
  } while (responseRestart != "y" &&
      responseRestart != "yes" &&
      responseRestart != "n" &&
      responseRestart != "no");

  // reset varaibles
  if (responseRestart == "y" || responseRestart == "yes") {
    rate = tripLength = daysUntilTrip = initialCost = 0;
    tripCost = discounts = savings = serviceCost = totalCost = 0;
    main();
  } else { cout << "\n"
      "╔╗ ┬ ┬┌─┐   ┬ ┬┌─┐┬  ┬┌─┐  ┌─┐  ┌┐ ┌─┐┌─┐┬ ┬┌┬┐┬┌─┐┬ ┬┬    ┌┬┐┬┌┬┐┌─┐┬\n"
      "╠╩╗└┬┘├┤    ├─┤├─┤└┐┌┘├┤   ├─┤  ├┴┐├┤ ├─┤│ │ │ │├┤ │ ││     │ ││││├┤ │\n"
      "╚═╝ ┴ └─┘┘  ┴ ┴┴ ┴ └┘ └─┘  ┴ ┴  └─┘└─┘┴ ┴└─┘ ┴ ┴└  └─┘┴─┘   ┴ ┴┴ ┴└─┘o\n"
      << endl;
  };

  return 0;
};

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


