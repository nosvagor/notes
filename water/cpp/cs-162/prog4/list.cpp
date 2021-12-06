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
    head->data.~entry();
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
void list::insert(node *& head) {

  // signals end of LLL.
  if (!head) {
    head = new node;
    head->data.read_manual();
    head->next = NULL;
  }

  // traverse until the end of LLL is reached.
  if (head->next) {
    insert(head->next);
    return;
  }

  // prompt to continue manual entries, if desired.
  if (yes_no("\nEntries exist. Add another entry?")) insert(head->next);

}



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
