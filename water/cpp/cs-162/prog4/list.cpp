// ┬  ┬┌─┐┌┬┐
// │  │└─┐ │
// ┴─┘┴└─┘ ┴
// cullyn --- cs162 --- program 4
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
  tail = NULL;
}

void list::build(node *& head, node *& tail, ifstream & in_file) {

  while (!in_file.eof()) {
    if (!head) {
      head = new node;
      head->data.read_auto(in_file);
      head->next = NULL;
    }

    if (!in_file.eof()) tail = head;
    build(head->next, tail, in_file);
  }
}

void list::destroy(node *& head) {
  if (!head) return;

  if (!head->next) {
    head->data.~entry();
    head = NULL;
    delete head;
  } else {
    destroy(head->next);
  }
}

list::~list() {
  head = NULL;
  tail = NULL;
}
//===========================================================================//


// ┬  ┬┌─┐┌┬┐  ┌─┐┬ ┬┌┐┌┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
// │  │└─┐ │   ├┤ │ │││││   │ ││ ││││└─┐
// ┴─┘┴└─┘ ┴   └  └─┘┘└┘└─┘ ┴ ┴└─┘┘└┘└─┘
//===========================================================================//

void list::insert(node *& head) {

  if (!head) {
    head = new node;
    head->data.read_manual();
    head->next = NULL;
  }

  if (head->next) {
    insert(head->next);
    return;
  }

  if (yes_no("\nEntries exist. Add another entry?")) insert(head->next);

}

void list::display_all(node *& head) {

  if (!head) return;

  head->data.display();
  display_all(head->next);
}
//===========================================================================//
