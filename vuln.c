#include <stdio.h>
#include <string.h>

//intentionally vulnerable c program https://www.rootnetsec.com/buffer-overflow/

int main(void)
{
  char buff[32];
  int pass = 0;

  printf("\n Enter the password : \n");
  gets(buff);

  if(strcmp(buff, "strongpassword"))
  {
    printf ("\n Wrong password \n");
  }
  else
  {
    printf ("\n Correct password \n");
    pass = 1;
  }

  if(pass)
  {
    printf ("\n This is the secret guarded by the strongpassword ! \n");
  }

  return 0;



}
