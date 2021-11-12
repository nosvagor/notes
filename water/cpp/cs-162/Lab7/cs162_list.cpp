#include "cs162_list.h"

// ┬  ┬┌─┐┌┬┐
// │  │└─┐ │
// ┴─┘┴└─┘ ┴

//Constructor
list::list() {
  head = NULL;
}


//Display all items in a linear linked list
void list::display_all()
{
  node * current = head;

  if (!head) return;

  while (current->next) {
    cout << current->data << endl;
    current = current->next;
  }

  cout << current->data << endl;

}


//Count the number of times the first node's data appears
//in the list, and return that count.
int list::count_first()
{
  int count {0};

  node * current = head;

  if (!head) return 0;


  while (current) {
    if (current->data == head->data) ++count;
    current = current->next;
  }

  return count;
}

//Display the LAST node's data
int list::get_last()
{

  node * current = head;

  if (!head) return 0;

  while (current->next) current = current->next;

  return current->data;
}

//Return true if the last node's data appears
//in the list more than once.
bool list::find_last()
{
  int last {0};

  last = get_last();

  node * current = head;

  while (current->next) {
    if (current->data == last) return true;
    current = current->next;
  }

  return false;
}
