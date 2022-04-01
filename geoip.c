#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
   char command[50];

   strcpy( command, "python3 /etc/GeoIP/geoip.py" );
   system(command);

   return(0);
} 