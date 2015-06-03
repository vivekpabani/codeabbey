#include <stdio.h>
#include <math.h>
/*
Problem Definition -
Now you will be given several pairs of values and you need to calculate sum for each pair.
Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves - one pair at each line.
Answer should contain the results separated by spaces.
*/

int main(int argc, char *argv[]){
  int count=0, i, start=2, sum=0;  
  /* Take Count */
  if ( argc != 2 ) /* argc should be 2 for correct execution */ 
  {
    count = atoi(argv[1]);
  }
  
  /* loop over pairs*/
  for(i=0; i<count; ++i)
  {
    sum = atoi(argv[start]) + atoi(argv[start+1]);
    printf("%d\n",sum);
    start+=2;
  }
}
  /* sum of ech pair*/
  return 1;
}
