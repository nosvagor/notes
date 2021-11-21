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

void list::build(node *& head, ifstream & in_file) {

  while (!in_file.eof()) {
    if (!head) {
      head = new node;
      head->data.read_auto(in_file);
      head->next = NULL;
    }

    build(head->next, in_file);
  }
}

void list::destroy(node *& head) {

}

// destructor
list::~list() {


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

  if (yes_no("Add another entry?")) insert(head->next);

}

void list::display_all(node *& head) {

  if (!head) return;

  head->data.display();
  display_all(head->next);
}
//===========================================================================//
