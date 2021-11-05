// ╔═╗┬  ┌─┐┌─┐┌─┐  ┬┌┬┐┌─┐┬  ┌─┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐┬┌┬┐┌─┐┌┐┌┌─┐
// ║  │  ├─┤└─┐└─┐  ││││├─┘│  ├┤ │││├┤ │││ │ ├─┤│ │ │ ││││└─┐
// ╚═╝┴─┘┴ ┴└─┘└─┘  ┴┴ ┴┴  ┴─┘└─┘┴ ┴└─┘┘└┘ ┴ ┴ ┴┴ ┴ └─┘┘└┘└─┘
// cullyn --- cs162
// Purpose: this file implementations class methods and constructors.

#include "main.h"

// Animal constructor
animal::animal() {
  name[0] = '\0';
  species[0] = '\0';
  breed[0] = '\0';
  service[0] = '\0';
  misc[0] = '\0';
}
