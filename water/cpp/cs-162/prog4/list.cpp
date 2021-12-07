// ┬  ┬┌─┐┌┬┐
// │  │└─┐ │
// ┴─┘┴└─┘ ┴
// cullyn --- cs162 --- program 5
// Purpose: this file implements the class list methods, used for for managing
// the list of syntax entries)

//===========================================================================//
  #include "header.h"
//===========================================================================//

// ┬  ┬┌─┐┌┬┐  ┌┬┐┌─┐┌┐┌┌─┐┌─┐┌─┐┌┬┐┌─┐┌┐┌┌┬┐
// │  │└─┐ │   │││├─┤│││├─┤│ ┬├┤ │││├┤ │││ │
// ┴─┘┴└─┘ ┴   ┴ ┴┴ ┴┘└┘┴ ┴└─┘└─┘┴ ┴└─┘┘└┘ ┴
//===========================================================================//
// constructor
list::list() {
  head = NULL;
}


// automatic build using external file
void list::build(node *& head, ifstream & in_file) {

  // continue to append new nodes while each new line in read in.
  while (!in_file.eof()) {
    if (!head) {
      head = new node;
      head->data.read_auto(in_file);
      head->next = NULL;
    }

    build(head->next, in_file);
  }
}


// recursive destructor
void list::destroy(node *& head) {
  if (!head) return;

  if (!head->next) {
    head->data.~entry(); // delete dynamically allocated memory of each entry
    head = NULL;
    delete head;
  } else {
    destroy(head->next);
    head = NULL;
    delete head;
  }
}
// destructor (do I need this?)
list::~list() {
  head = NULL;
}
//===========================================================================//


// ┬  ┬┌─┐┌┬┐  ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// │  │└─┐ │   ├┤ │ │││││   │ ││ ││││└─┐
// ┴─┘┴└─┘ ┴   └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘
//===========================================================================//


// insert inserts a new entry class object and end of a LLL via manual entry.
void list::insert(node *& head, bool &another) {

  // signals end of LLL.
  if (!head) {
    head = new node;
    head->data.read_manual();
    head->next = NULL;
  }

  // traverse until the end of LLL is reached.
  if (head->next) {
    insert(head->next, another);
    return;
  }

  // end recursion if answer is no.
  another = yes_no("\nAdd another entry?");
  if (!another) return;

  // continue adding new nodes
  insert(head->next, another);
}


// ============================================================================
// ┌─┐┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐  ┌─┐┬┬  ┬┌─┐  ┌─┐┌─┐┌┐┌┌┬┐┌─┐┌┐┌┌┬┐
// ├─┘├┬┘│ ││ ┬├┬┘├─┤│││  ├┤ │└┐┌┘├┤   │  │ ││││ │ ├┤ │││ │
// ┴  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴  └  ┴ └┘ └─┘  └─┘└─┘┘└┘ ┴ └─┘┘└┘ ┴

// primitive attempt at swapping nodes. Couldn't figure out how to swap them,
// so i swapped the data instead. I know this is not ideal, but it worked, ish.
bool list::swap(node *& head) {

  bool swap = false;

  if (head->data.name[0] > head->next->data.name[0]) swap = true;

  if (swap) {
    node *temp = new node;
    temp->data = head->data;

    head->data = head->next->data;
    head->next->data = temp->data;

    temp = NULL;
    delete temp;
  }

  return swap;
}

// primitive attempt at a recursive bubble sort. I think the way I implemented
// has even worse time-space complexity, but I tried... I failed to get it to
// restart once an entry is sorted, so I just call it several times in main.
void list::sort(node *& head) {

  // check to see if list is empty, or if end of list is reached. If end of
  // list is reached, it signals the entry has been sorted.
  if (!head || !head->next->data.name) return;

  bool swapped = false;

  // check to see if elements need to be swapped, return true if the were.
  swapped = swap(head);

  // restart sorting from beginning if element is swapped. (bubbling)
  if (swapped) {
    sort(head);
    return;
  }

  // if element is not swapped, then continue to check next two elements.
  if (head->next) sort(head->next);

  return;
}

//=============================================================================

// display_all displays data of each syntax entry in the entire LLL.
void list::display_all(node *& head) {

  if (!head) return;

  head->data.display();
  display_all(head->next);
}


// search finds any matches, based on search criteria passed in from a switch
// statement in main.
int list::search(char query[SIZE], node *& head, int search_select) {

  int count {0}; // used to list number of matches

  if (!head) return 0;

  // recursively call function, added to count for each valid comparison.
  if (head->next) {
    if (head->data.compare(query, search_select)) {
      head->data.display();
      ++count;
    }
    count += search(query, head->next, search_select);
  }

  return count;
}


// edit behaves similar to search, but calls the entry edit function on the
// first match found.
void list::edit(char name[SIZE], node *& head) {

  if (!head) return;

  if (head->next) {
    if (head->data.compare(name, 1)) {
      head->data.edit();
      return;
    } else {
      edit(name, head->next);
    }
  }

  return;
}


//===========================================================================//
