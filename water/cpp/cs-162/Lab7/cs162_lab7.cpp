#include "cs162_list.h"

int main()
{
    list my_list;
    my_list.build();

    my_list.display_all();
    cout << "\nNumber of head occurrence: " << my_list.count_first() << endl;
    cout << "\nTail: " << my_list.get_last() << endl;
    cout << "\nTail duplicates?: " << my_list.find_last() << endl;

    return 0;
}
