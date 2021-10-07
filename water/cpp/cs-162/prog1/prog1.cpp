/* ╔═╗┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ╔═╗┌┐┌┌─┐ */
/* ╠═╝├┬┘│ ││ ┬├┬┘├─┤│││  ║ ║│││├┤  */
/* ╩  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴  ╚═╝┘└┘└─┘ */
/* Cullyn Newamn --- CS 162 */
/* Purpose: calculate the price of a rental stay, accounting for potential
 * discounts or fees.  */

#include <iostream>
#include <ctime>
using namespace std;

void greeting();
void data();
void errorCheck();
void calculate();
void calculateDiscounts();
void results();

int main() {
  greeting();
  data();
  return 0;
}

void greeting(){
  cout << "Welcome to 'The Actual Price'" << endl;
  cout << "Simply provide the nightly rate, start date, and end date of your "
          "vacation!\nWe will calculate the actual price, accounting for any "
          "fees and discounts."
  << endl;

  cout << "Default fees and discounts include:\n\
    \t - 20\% discount for booking more than 5 days in advance \n\
    \t - 10\% discount for stays longer than 3 days \n\
    \t - $50 cleaning fee for says longer than 3 days \n\
    \t - 1\% service fee (applied prior to discounts)"
  << endl << endl;
}

void data(){
  int rate = 0;
  int date = 0;

  auto getRate = [&](){
    cout << "Nightly rate (USD): ";
    cin >> rate;
    return rate;
  };

/*   auto getStartDate = [&](){ */
/*     cout << "Start date (): "; */
/*     cin >> startDate; */
/*     return rate; */
/*   }; */

  getRate();
  while (rate <= 0) {
    cout << "Rate invalid, please enter amount that is great than zero" << endl;
    getRate();
  };

  cout << "Nightly rate is $" << rate << endl;
}
